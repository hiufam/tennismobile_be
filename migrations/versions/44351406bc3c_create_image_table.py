"""Create image table

Revision ID: 44351406bc3c
Revises: d2016f232654
Create Date: 2023-10-12 00:55:16.279701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44351406bc3c'
down_revision: Union[str, None] = 'd2016f232654'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'images',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('url', sa.String, nullable=False)
    )


def downgrade() -> None:
    op.drop_table('images')