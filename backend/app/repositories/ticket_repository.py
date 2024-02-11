import json
from typing import Optional

class TicketRepository:
    def __init__(self, filepath: str):
        with open(filepath) as json_file:
            raw_data = json.load(json_file)
            self.ticket_dict = {ticket["id"]: (ticket | {"index": index}) for index, ticket in enumerate(raw_data["tickets"])}
            self.message_dict = {message["id"]: message for message in raw_data["messages"]}

    def get_tickets(self, limit: Optional[int] = None) -> list[dict]:
        return list(self.ticket_dict.values())[:limit]
    
    def get_messages(self, limit: Optional[int] = None) -> list[dict]:
        return list(self.message_dict.values())[:limit]
    
    def get_messages_by_id(self, message_ids: list[int]) -> list[dict]:
        return [self.message_dict[message_id] for message_id in message_ids]
    
    def delete_ticket(self, ticket_id: int):
        del self.ticket_dict[ticket_id]
