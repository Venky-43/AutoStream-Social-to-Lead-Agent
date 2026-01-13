import json

class KnowledgeBase:
    def __init__(self, path="data/knowledge_base.json"):
        with open(path, "r") as f:
            self.data = json.load(f)

    def get_pricing_info(self):
        pricing = self.data["pricing"]
        response = []
        for plan, details in pricing.items():
            response.append(
                f"{plan}: {details['price']} – {', '.join(details['features'])}"
            )
        return "\n".join(response)

    def get_policies(self):
        policies = self.data["policies"]
        return f"Refund Policy: {policies['refund']}\nSupport: {policies['support']}"
