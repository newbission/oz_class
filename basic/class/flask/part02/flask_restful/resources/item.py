from flask_restful import Resource, request

items = []  # 임시 db역할


class Item(Resource):
    # 특정 아이템 조회
    def get(self, name):
        for item in items:
            if item["name"] == name:
                return item
        return {"message": "Item not found"}, 404

    # 새 아이템 추가
    def post(self, name):
        for item in items:
            if item["name"] == name:
                return {
                    "message": f"An item with name '{name}' is already exists."
                }, 400

        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201

    # 아이템 수정
    def put(self, name):
        data = request.get_json()
        for item in items:
            if item["name"] == name:
                item["price"] = data["price"]
                return item

        # 아이템이 존재하지 않으면 새로운 아이템을 추가
        new_item = {"name": name, "price": data["price"]}
        items.append(new_item)
        return new_item

    # 아이템 삭제
    def delete(self, name):
        global items
        items = [item for item in items if item["name"] != name]
        return {"message": "Item deleted"}
