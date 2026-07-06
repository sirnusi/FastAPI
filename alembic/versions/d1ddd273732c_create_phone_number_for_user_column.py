"""Create phone number for user column

Revision ID: d1ddd273732c
Revises: 
Create Date: 2026-06-16 09:12:46.992453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd1ddd273732c'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
   pass
  


def downgrade() -> None:
    """Downgrade schema."""
    pass
