"""Create related tables: link, click

Revision ID: 4ef869ff01c2
Revises: 
Create Date: 2023-06-03 23:04:01.713134

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4ef869ff01c2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('link',
    sa.Column('token', sa.VARCHAR(length=9), autoincrement=False, nullable=False),
    sa.Column('long_link', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('activation_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('deactivation_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('token', name='link_pkey'),
    sa.UniqueConstraint('long_link', name='link_long_link_key'),
    postgresql_ignore_search_path=False
    )
    op.create_table('click',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('link_token', sa.VARCHAR(length=9), autoincrement=False, nullable=True),
    sa.Column('user_ip', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('date', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['link_token'], ['link.token'], name='click_link_token_fkey'),
    sa.PrimaryKeyConstraint('id', name='click_pkey')
    )
    op.create_index('ix_click_id', 'click', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_click_id', table_name='click')
    op.drop_table('click')
    op.drop_table('link')
