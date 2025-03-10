"""Populate initial trade data

Revision ID: 931c2cb4638c
Revises: fc1eb038fcc2
Create Date: 2025-03-10 14:58:56.082197

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '931c2cb4638c'
down_revision: Union[str, None] = 'fc1eb038fcc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Insert initial trade data."""
    op.execute("""
        INSERT INTO trade_data (market, price, timestamp)
        VALUES
            ('Wheat', 250.75, NOW()),
            ('Corn', 180.50, NOW()),
            ('Rice', 320.25, NOW()),
            ('Soybeans', 200.00, NOW());
    """)


def downgrade() -> None:
    """Remove seeded data."""
    op.execute("DELETE FROM trade_data WHERE market IN ('Wheat', 'Corn', 'Rice', 'Soybeans');")
