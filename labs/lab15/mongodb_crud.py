from pymongo import MongoClient

def main():
    # Connect to local MongoDB
    client = MongoClient("mongodb://localhost:27017/")

    # Create/use database
    db = client["company"]

    # Create/use collection
    employees = db["employees"]

    # Clean collection for repeatable runs
    employees.delete_many({})

    # Insert documents
    employees.insert_many([
        {"name": "Alice", "age": 30, "dept": "HR"},
        {"name": "Bob", "age": 25, "dept": "IT"}
    ])
    print("Inserted employees")

    # Read documents
    print("Employees:")
    for emp in employees.find():
        print(emp)

    # Update a document
    employees.update_one({"name": "Alice"}, {"$set": {"age": 31}})
    print("Updated Alice's age")

    # Delete a document
    employees.delete_one({"name": "Bob"})
    print("Deleted Bob")

    # Final list
    print("Final Employees:")
    for emp in employees.find():
        print(emp)

    client.close()

if __name__ == "__main__":
    main()
