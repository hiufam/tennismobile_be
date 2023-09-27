"""Add user table

Revision ID: d2016f232654
Revises: 
Create Date: 2023-09-27 11:38:34.993416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from api.models.user import Gender

# revision identifiers, used by Alembic.
revision: str = 'd2016f232654'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True), 
        sa.Column('phone_number', sa.String(10), nullable=False),
        sa.Column('facebook_account', sa.String(50), nullable=True),
        sa.Column('google_account', sa.String(50), nullable=True),
        sa.Column('full_name', sa.String, nullable=True),
        sa.Column('date_of_birth', sa.Date, nullable=True),
        sa.Column('gender', sa.Enum(Gender), nullable=True),
        sa.Column('singles_skill', sa.Integer, nullable=False, default=0),
        sa.Column('doubles_skill', sa.Integer, nullable=False, default=0),
        sa.Column('avatar', sa.String, nullable=True),
        sa.Column('registration_otp', sa.String, nullable=True),
        sa.Column('registration_otp_expiration', sa.DateTime, nullable=True),
        sa.Column('is_verify', sa.Boolean, nullable=False, default=False),
    )
    op.create_unique_constraint(None, 'users', ['phone_number'])


def downgrade() -> None:
    op.drop_table('users')
