from compas.data import DataDecoder
from compas.data import DataEncoder

from specklepy.objects import Base


class SpeckleDataBridge(Base):
    data: dict = {}

    @classmethod
    def from_compas(cls, compas_obj):
        encoder = DataEncoder()
        return cls(data=encoder.default(compas_obj))

    def to_compas(self):
        decoder = DataDecoder()
        return decoder.object_hook(self.data)


if __name__ == '__main__':

    import compas
    from compas.datastructures import Mesh
    from compas.utilities import flatten

    from specklepy.objects.geometry import Mesh as SMesh
    from specklepy.api import operations
    from specklepy.api.client import SpeckleClient
    from specklepy.transports.server import ServerTransport

    mesh = Mesh.from_obj(compas.get('tubemesh.obj'))
    print(mesh)

    def mesh_to_vertices_and_faces(mesh: Mesh):
        vertices, faces = mesh.to_vertices_and_faces()
        triangles = []
        for face in faces:
            triangles.append([len(face), *face])
        return list(flatten(vertices)), list(flatten(triangles))


    vertices, faces = mesh_to_vertices_and_faces(mesh)
    smesh = SMesh(vertices=vertices, faces=faces)
    smesh["compas"] = SpeckleDataBridge.from_compas(mesh)

    client = SpeckleClient(host="speckle.xyz")
    client.authenticate_with_token(token="e0143e759ed36fb808fe365910d855066154ab6c4c")

    # commit the object data to the server
    stream_id = 'bd64112e8c'
    transport = ServerTransport(client=client, stream_id=stream_id)
    object_id = operations.send(base=smesh, transports=[transport])
    commid_id = client.commit.create(stream_id=stream_id, object_id=object_id, message='Mesh sent from compas!')


    # read the object back
    transport = ServerTransport(client=client, stream_id=stream_id)
    smesh = operations.receive(object_id, transport)
    mesh_received = smesh["compas"].to_compas()
    print(mesh_received)