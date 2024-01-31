from compas_cloud import Proxy
from compas.geometry import Translation

proxy = Proxy(host='127.0.0.1', port=9009)


# transform_points_numpy = proxy.function('compas.geometry.transform_points_numpy')
# T = Translation.from_vector([0, 0, 1])
# points = [[0,0,0], [1,0,0]]
# translated_points = transform_points_numpy(points, T) # This calculation will be excuted on the server-side
# print(translated_points)


transform_points_numpy = proxy.function('compas.geometry.transform_points_numpy', cache=True)

T = Translation.from_vector([0, 0, 1])
T = proxy.cache(T) # This will cache the object on the server-side
print("Translation", T) # This will print the reference to the object on the server-side

points = [[0,0,0], [1,0,0]]
for i in range(100):
    translated_points = transform_points_numpy(points, T) # This calculation will be excuted on the server-side
    points = translated_points

print(translated_points) # This will print the reference to the object on the server-side
print(proxy.get(translated_points)) # This will retrieve the object from the server