"""Drop node_public_key table

Revision ID: e8f2c4b6d9a1
Revises: c6b1d8f2a9e3
Create Date: 2026-05-25 00:00:00.000000

"""

from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e8f2c4b6d9a1"
down_revision: str | None = "c6b1d8f2a9e3"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.drop_index("idx_node_public_key_public_key", table_name="node_public_key")
    op.drop_index("idx_node_public_key_node_id", table_name="node_public_key")
    op.drop_table("node_public_key")


def downgrade() -> None:
    op.create_table(
        "node_public_key",
        sa.Column("id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("node_id", sa.BigInteger(), nullable=False),
        sa.Column("public_key", sa.String(), nullable=False),
        sa.Column("first_seen_us", sa.BigInteger(), nullable=True),
        sa.Column("last_seen_us", sa.BigInteger(), nullable=True),
    )
    op.create_index("idx_node_public_key_node_id", "node_public_key", ["node_id"], unique=False)
    op.create_index(
        "idx_node_public_key_public_key",
        "node_public_key",
        ["public_key"],
        unique=False,
    )
