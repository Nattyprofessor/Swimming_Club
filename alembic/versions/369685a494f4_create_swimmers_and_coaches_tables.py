"""Create swimmers and coaches tables

Revision ID: 369685a494f4
Revises: 
Create Date: 2024-12-18 23:14:50.429734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '369685a494f4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('swimmers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('style', sa.String(), nullable=True),
    sa.Column('best_lap', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_swimmers_id'), 'swimmers', ['id'], unique=False)
    op.create_index(op.f('ix_swimmers_name'), 'swimmers', ['name'], unique=False)
    op.create_table('coaches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('swimmer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['swimmer_id'], ['swimmers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_coaches_id'), 'coaches', ['id'], unique=False)
    op.create_index(op.f('ix_coaches_name'), 'coaches', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_coaches_name'), table_name='coaches')
    op.drop_index(op.f('ix_coaches_id'), table_name='coaches')
    op.drop_table('coaches')
    op.drop_index(op.f('ix_swimmers_name'), table_name='swimmers')
    op.drop_index(op.f('ix_swimmers_id'), table_name='swimmers')
    op.drop_table('swimmers')
    # ### end Alembic commands ###