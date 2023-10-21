"""create equipment table

Revision ID: d2502aa80369
Revises: 44351406bc3c
Create Date: 2023-10-18 08:28:24.124914

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from api.models.user_equipment import Backhand, Forehand, DominatHand, ClothingSize


# revision identifiers, used by Alembic.
revision: str = 'd2502aa80369'
down_revision: Union[str, None] = '44351406bc3c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'user_equipments',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
        sa.Column('backhand', sa.Enum(Backhand)),
        sa.Column('forehand', sa.Enum(Forehand)),
        sa.Column('dominant_hand', sa.Enum(DominatHand)),
        sa.Column('clothing_size', sa.Enum(ClothingSize)),
        sa.Column('shoes_size', sa.Integer),

        sa.Column('racket_brand_id', sa.Integer),
        sa.Column('racket_parameter_id', sa.Integer),
        sa.Column('racket_string_id', sa.Integer),
        sa.Column('ball_brand_id', sa.Integer),
        sa.Column('clothing_brand_id', sa.Integer),
        sa.Column('shoes_brand_id', sa.Integer),
    )

def downgrade() -> None:
    op.drop_table('user_equipments')
