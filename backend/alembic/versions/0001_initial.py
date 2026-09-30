"""Create prediction and anomaly history tables."""
from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table("predictions", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("origin_yard", sa.String(80), nullable=False), sa.Column("destination_yard", sa.String(80), nullable=False), sa.Column("predicted_delay_hours", sa.Float(), nullable=False), sa.Column("on_time_probability", sa.Float(), nullable=False), sa.Column("risk_level", sa.String(20), nullable=False), sa.Column("model_version", sa.String(80), nullable=False), sa.Column("created_at", sa.DateTime(), nullable=False))
    op.create_table("anomaly_alerts", sa.Column("id", sa.Integer(), primary_key=True), sa.Column("yard_id", sa.String(80), nullable=False), sa.Column("anomaly_score", sa.Float(), nullable=False), sa.Column("is_anomaly", sa.Boolean(), nullable=False), sa.Column("severity", sa.String(20), nullable=False), sa.Column("explanation", sa.Text(), nullable=False), sa.Column("created_at", sa.DateTime(), nullable=False))

def downgrade() -> None:
    op.drop_table("anomaly_alerts")
    op.drop_table("predictions")
