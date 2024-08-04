from pinecone import Pinecone

pc = Pinecone(api_key="API-KEY")
index = pc.Index("INDEX-HERE")


index.upsert(
    vectors=[
        {
            "id": "vec1", 
            "values": [0.1, 0.1], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec2", 
            "values": [0.2, 0.2], 
            "metadata": {"genre": "action"}
        }, {
            "id": "vec3", 
            "values": [0.3, 0.3], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec4", 
            "values": [0.4, 0.4], 
            "metadata": {"genre": "action"}
        }
    ],
    namespace= "ns1"
)