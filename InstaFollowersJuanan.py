import instaloader
import pandas as pd

# Iniciar sesión en Instagram
L = instaloader.Instaloader()

USERNAME = ''
PASSWORD = ''

L.login(USERNAME, PASSWORD)

profile = instaloader.Profile.from_username(L.context, USERNAME)

# Obtener seguidos
following = set(profile.get_followees())

# Obtener seguidores
followers = set(profile.get_followers())

# Encontrar cuentas que sigues pero que no te siguen de vuelta
not_following_back = following - followers

# Convertir a lista para manipulación más fácil
not_following_back_list = [user.username for user in not_following_back]

# Guardar en un archivo CSV
df = pd.DataFrame(not_following_back_list, columns=['Username'])
df.to_csv('not_following_back.csv', index=False)

print(f"Usuarios que no te siguen de vuelta: {len(not_following_back_list)}")
print(not_following_back_list)