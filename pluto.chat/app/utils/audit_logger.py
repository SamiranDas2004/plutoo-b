"""
Audit Logging System
Logs all security-relevant events
"""
import logging
from datetime import datetime
from sqlalchemy.orm import Session
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/audit.log'),
        logging.StreamHandler()
    ]
)

audit_logger = logging.getLogger('audit')


class AuditLogger:
    """Centralized audit logging"""
    
    @staticmethod
    def log_auth_attempt(
        email: str,
        success: bool,
        ip_address: str,
        action: str = "login",
        reason: Optional[str] = None
    ):
        """Log authentication attempts"""
        status = "SUCCESS" if success else "FAILED"
        message = f"AUTH_{action.upper()}_{status} | Email: {email} | IP: {ip_address}"
        if reason:
            message += f" | Reason: {reason}"
        
        if success:
            audit_logger.info(message)
        else:
            audit_logger.warning(message)
    
    @staticmethod
    def log_api_access(
        user_id: Optional[int],
        endpoint: str,
        method: str,
        ip_address: str,
        status_code: int
    ):
        """Log API access"""
        user_info = f"User: {user_id}" if user_id else "User: Anonymous"
        message = f"API_ACCESS | {user_info} | {method} {endpoint} | Status: {status_code} | IP: {ip_address}"
        audit_logger.info(message)
    
    @staticmethod
    def log_security_event(
        event_type: str,
        description: str,
        ip_address: str,
        user_id: Optional[int] = None,
        severity: str = "WARNING"
    ):
        """Log security events"""
        user_info = f"User: {user_id}" if user_id else "User: Anonymous"
        message = f"SECURITY_EVENT | Type: {event_type} | {user_info} | IP: {ip_address} | {description}"
        
        if severity == "CRITICAL":
            audit_logger.critical(message)
        elif severity == "ERROR":
            audit_logger.error(message)
        else:
            audit_logger.warning(message)
    
    @staticmethod
    def log_data_access(
        user_id: int,
        action: str,
        resource_type: str,
        resource_id: Optional[str] = None,
        ip_address: str = "unknown"
    ):
        """Log data access (CRUD operations)"""
        resource_info = f"{resource_type}"
        if resource_id:
            resource_info += f":{resource_id}"
        
        message = f"DATA_ACCESS | User: {user_id} | Action: {action} | Resource: {resource_info} | IP: {ip_address}"
        audit_logger.info(message)
    
    @staticmethod
    def log_rate_limit_exceeded(
        ip_address: str,
        endpoint: str,
        limit: str
    ):
        """Log rate limit violations"""
        message = f"RATE_LIMIT_EXCEEDED | IP: {ip_address} | Endpoint: {endpoint} | Limit: {limit}"
        audit_logger.warning(message)


def get_client_ip(request) -> str:
    """Extract client IP from request"""
    # Check for proxy headers
    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        return forwarded.split(",")[0].strip()
    
    real_ip = request.headers.get("X-Real-IP")
    if real_ip:
        return real_ip
    
    # Fallback to direct connection
    if request.client:
        return request.client.host
    
    return "unknown"
