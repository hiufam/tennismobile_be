"""create equipment table

Revision ID: d2502aa80369
Revises: 44351406bc3c
Create Date: 2023-10-18 08:28:24.124914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd2502aa80369'
down_revision: Union[str, None] = '44351406bc3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'equipments',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('racket_brand', sa.String),
        sa.Column('racket_parameter', sa.String),
        sa.Column('racket_string', sa.String),
        sa.Column('backhand', sa.String),
        sa.Column('forehand', sa.String),
        sa.Column('dominant_hand', sa.String),
        sa.Column('ball_brand', sa.String),
        sa.Column('clothing_brand', sa.String),
        sa.Column('clothing_size', sa.String),
        sa.Column('shoes_brand', sa.String),
        sa.Column('shoes_size', sa.String),
    )

def downgrade() -> None:
    op.drop_table('equipments')
