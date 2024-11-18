bags = [
    { "model_no": "B001" ,"COLOR" : "RED AND WHITE ","size": "small ",
        "age_group":"15+"},
    { "model_no": "B002" , "COLOR" : "BLUE OCEAN  ","size": "MEDIUM ",
        "age_group":"18+" },
    {"model_no": "B003" ,"COLOR" : "GREEN FOREST  ","size": "LARGE ",
        "age_group": "20+"},
    {"model_no": "B003" ,"COLOR" : "GREEN FOREST  ","size": "LARGE ",
        "age_group":"25+"}
    
        
]

# Function to search for a bag by model number
def search_bag(model_no):
    for bag in bags:
        if bag["model_no"] == model_no:
            return bag
    return "Bag not found."


# Prompt the user for a model number to search
model_no_to_search = input("Enter the model number of the bag you want to search for: ")
bag_details = search_bag(model_no_to_search)
print(bag_details)


# # Prompt the user for a model number to search
# model_no_to_search = input("Enter the model number of the bag you want to search for: ")
# bag_details = search_bag(model_no_to_search)
# print(bag_details)
# # Define the details of 10 different bag models
# bags = [
#     {"model_no": "B001", "color": "Red", "size": "Small", "details": "Red small bag, perfect for casual outings."},
#     {"model_no": "B002", "color": "Blue", "size": "Medium", "details": "Blue medium bag, ideal for daily use."},
#     {"model_no": "B003", "color": "Black", "size": "Large", "details": "Black large bag, great for travel."},
#     {"model_no": "B004", "color": "Green", "size": "Small", "details": "Green small bag, compact and stylish."},
#     {"model_no": "B005", "color": "Yellow", "size": "Medium", "details": "Yellow medium bag, bright and spacious."},
#     {"model_no": "B006", "color": "White", "size": "Large", "details": "White large bag, elegant and roomy."},
#     {"model_no": "B007", "color": "Pink", "size": "Small", "details": "Pink small bag, cute and trendy."},
#     {"model_no": "B008", "color": "Purple", "size": "Medium", "details": "Purple medium bag, stylish and versatile."},
#     {"model_no": "B009", "color": "Brown", "size": "Large", "details": "Brown large bag, durable and practical."},
#     {"model_no": "B010", "color": "Grey", "size": "Small", "details": "Grey small bag, sleek and modern."},
# ]

# # Function to search for a bag by model number
# def search_bag(model_no):
#     for bag in bags:
#         if bag["model_no"] == model_no:
#             return bag
#     return "Bag not found."

# # Prompt the user for a model number to search
# model_no_to_search = input("Enter the model number of the bag you want to search for: ")
# bag_details = search_bag(model_no_to_search)
# print(bag_details)
