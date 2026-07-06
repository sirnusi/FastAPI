"""Create phone number for users column

Revision ID: 21570dcd2d34
Revises: d1ddd273732c
Create Date: 2026-06-16 10:39:05.541906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '21570dcd2d34'
down_revision: Union[str, Sequence[str], None] = 'd1ddd273732c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users', sa.Column("phone_number", sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    
