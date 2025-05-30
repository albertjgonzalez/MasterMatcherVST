import json
from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any
from enum import Enum
import logging

logger = logging.getLogger(__name__)

class MessageType(Enum):
    """Enum for different message types"""
    PROCESS_REQUEST = "process_request"
    PROCESS_RESPONSE = "process_response"
    STATUS_UPDATE = "status_update"
    ERROR = "error"
    PING = "ping"
    PONG = "pong"

class ProtocolError(Exception):
    """Base exception for protocol-related errors"""
    pass

class InvalidMessageError(ProtocolError):
    """Raised when a message is invalid or malformed"""
    pass

class MessageTimeoutError(ProtocolError):
    """Raised when a message times out"""
    pass

@dataclass
class Message:
    """Base message class"""
    type: MessageType
    payload: Dict[str, Any]

    def to_json(self) -> str:
        """Convert message to JSON string"""
        return json.dumps({
            "type": self.type.value,
            "payload": self.payload
        })

    @classmethod
    def from_json(cls, json_str: str) -> 'Message':
        """Create message from JSON string"""
        try:
            data = json.loads(json_str)
            msg_type = MessageType(data["type"])
            return cls(type=msg_type, payload=data["payload"])
        except (json.JSONDecodeError, KeyError, ValueError) as e:
            logger.error(f"Error parsing message: {e}")
            raise InvalidMessageError(f"Invalid message format: {e}")

@dataclass
class ProcessRequest:
    """Message for requesting audio processing"""
    user_track: str
    reference_track: str
    output_path: str
    intensity: float = 1.0
    reference_weight: float = 0.5

    def to_message(self) -> Message:
        return Message(
            type=MessageType.PROCESS_REQUEST,
            payload=asdict(self)
        )

@dataclass
class ProcessResponse:
    """Message for processing response"""
    status: str
    output_path: Optional[str] = None
    message: str = ""
    processing_time: float = 0.0

    def to_message(self) -> Message:
        return Message(
            type=MessageType.PROCESS_RESPONSE,
            payload=asdict(self)
        )

@dataclass
class StatusUpdate:
    """Message for status updates"""
    status: str
    progress: float = 0.0
    message: str = ""

    def to_message(self) -> Message:
        return Message(
            type=MessageType.STATUS_UPDATE,
            payload=asdict(self)
        )

def validate_message(message: Message) -> bool:
    """Validate a message based on its type"""
    try:
        if message.type == MessageType.PROCESS_REQUEST:
            required_fields = ["user_track", "reference_track", "output_path"]
            if not all(field in message.payload for field in required_fields):
                raise InvalidMessageError("Missing required fields in process request")
        elif message.type == MessageType.PROCESS_RESPONSE:
            required_fields = ["status", "message"]
            if not all(field in message.payload for field in required_fields):
                raise InvalidMessageError("Missing required fields in process response")
        elif message.type == MessageType.STATUS_UPDATE:
            required_fields = ["status"]
            if not all(field in message.payload for field in required_fields):
                raise InvalidMessageError("Missing required fields in status update")
        return True
    except KeyError as e:
        logger.error(f"Missing required field: {e}")
        raise InvalidMessageError(f"Missing required field: {e}")

# Example usage
def create_process_request(user_track: str, reference_track: str, output_path: str) -> str:
    """Create a process request message"""
    request = ProcessRequest(
        user_track=user_track,
        reference_track=reference_track,
        output_path=output_path
    )
    return request.to_message().to_json()

def create_process_response(status: str, output_path: Optional[str] = None, message: str = "") -> str:
    """Create a process response message"""
    response = ProcessResponse(
        status=status,
        output_path=output_path,
        message=message
    )
    return response.to_message().to_json()

def create_status_update(status: str, progress: float = 0.0, message: str = "") -> str:
    """Create a status update message"""
    update = StatusUpdate(
        status=status,
        progress=progress,
        message=message
    )
    return update.to_message().to_json()
