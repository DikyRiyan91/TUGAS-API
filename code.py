import graphene
import mysql.connector

# Buat koneksi ke database MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='nama_database'
)

# Definisikan tipe objek GraphQL
class UserType(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Query(graphene.ObjectType):
    user = graphene.Field(UserType, id=graphene.Int())

    def resolve_user(root, info, id):
        # Menggunakan koneksi ke database untuk mengambil data dari MySQL
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        cursor.close()

        # Mengembalikan objek user berdasarkan ID yang diberikan
        if result:
            return UserType(id=result[0], name=result[1])
        return None

class CreateUser(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    user = graphene.Field(UserType)

    def mutate(root, info, name):
        # Menggunakan koneksi ke database untuk menyimpan data ke MySQL
        cursor = conn.cursor()
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (name,))
        conn.commit()
        cursor.close()

        # Mengembalikan objek user yang baru dibuat
        return CreateUser(user=UserType(id=cursor.lastrowid, name=name))

class UpdateUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    user = graphene.Field(UserType)

    def mutate(root, info, id, name):
        # Menggunakan koneksi ke database untuk mengupdate data di MySQL
        cursor = conn.cursor()
        query = "UPDATE users SET name = %s WHERE id = %s"
        cursor.execute(query, (name, id))
        conn.commit()
        cursor.close()

        # Mengembalikan objek user yang telah diupdate
        return UpdateUser(user=UserType(id=id, name=name))

class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.Int()

    user = graphene.Field(UserType)

    def mutate(root, info, id):
        # Menggunakan koneksi ke database untuk menghapus data dari MySQL
        cursor = conn.cursor()
        query = "DELETE FROM users WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        cursor.close()

        # Mengembalikan objek user yang telah dihapus
        return DeleteUser(user=UserType(id=id))

class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)

# Contoh penggunaan
query = '''
    mutation {
        createUser(name: "John") {
            user {
                id
                name
            }
        }
    }
'''
result = schema.execute(query)
print(result.data)

query = '''
    mutation {
        updateUser(id: 1, name: "John Doe") {
            user {
                id
                name
            }
        }
    }
'''
result = schema.execute(query)
print(result.data)

query = '''
    mutation {
        deleteUser(id: 1) {
            user {
                id
                name
            }
        }
    }
'''
result = schema.execute(query)
print(result.data)

query = '''
    query {
        user(id: 1) {
            id
            name
        }
    }
'''
result = schema.execute(query)
print(result.data)
