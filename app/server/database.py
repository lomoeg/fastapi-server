import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

# Database will be created if it doesn't already exist
database = client.chats

# Collections will be created if they don't already exist
chat_collection = database.get_collection("chats_collection")
message_collection = database.get_collection("message_collection")


# helpers -- return dict
def chat_helper(chat) -> dict:
    return {
        "id": str(chat["_id"]),
        "emotional_tone": chat["emotional_tone"],
        "operator": chat["operator"],
    }


def msg_helper(msg) -> dict:
    return {
        "id": str(msg["_id"]),
        "chat_id": msg["chat_id"],
        "msg_text": msg["msg_text"],
        "datetime": msg["datetime"],
        "emotional_tone": msg["emotional_tone"],
    }


# ------------------------------------------
# Defs for message collection
# ------------------------------------------

# Retrieve all messages from the chat with a matching ID
async def retrieve_all_msg_by_chat_id(id: str):
    msg_list = []
    async for msg in message_collection.find({"chat_id": id}):
        msg_list.append(msg_helper(msg))
    return msg_list


# Add a new message into to the database
async def add_new_msg(msg_data: dict) -> dict:
    msg = await message_collection.insert_one(msg_data)
    new_msg = await message_collection.find_one({"_id": msg.inserted_id})
    return msg_helper(new_msg)


# # Delete msg from
# async def delete_msg_collection():
#     async for msg in message_collection.find():
#         await message_collection.delete_one({"_id": ObjectId(id)})
#     return 1

# ------------------------------------------
# Defs for chat collection
# ------------------------------------------


# Retrieve all chats present in the database
async def retrieve_chat_list():
    chats = []
    async for chat in chat_collection.find():
        chats.append(chat_helper(chat))
    return chats


# Retrieve a chat with a matching ID
async def retrieve_chat(id: str) -> dict:
    chat = await chat_collection.find_one({"_id": ObjectId(id)})
    if chat:
        return chat_helper(chat)


# Add a new chat into to the database
async def add_chat(chat_data: dict) -> dict:
    chat = await chat_collection.insert_one(chat_data)
    new_chat = await chat_collection.find_one({"_id": chat.inserted_id})
    return chat_helper(new_chat)


# Update a chat with a matching ID
async def update_chat(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    chat = await chat_collection.find_one({"_id": ObjectId(id)})
    if chat:
        updated_chat = await chat_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_chat:
            return True
        return False
