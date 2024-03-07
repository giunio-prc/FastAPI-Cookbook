"""create sponsorships for many to many relationships

Revision ID: 9891059574b3
Revises: 4149f66b5194
Create Date: 2024-03-07 17:23:29.911339

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "9891059574b3"
down_revision: Union[str, None] = "4149f66b5194"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sponsors",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name"),
    )
    op.create_table(
        "sponsorships",
        sa.Column(
            "event_id", sa.Integer(), nullable=False
        ),
        sa.Column(
            "sponsor_id", sa.Integer(), nullable=False
        ),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["event_id"],
            ["events.id"],
        ),
        sa.ForeignKeyConstraint(
            ["sponsor_id"],
            ["sponsors.id"],
        ),
        sa.PrimaryKeyConstraint(
            "event_id", "sponsor_id"
        ),
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sponsorships")
    op.drop_table("sponsors")
    # ### end Alembic commands ###
