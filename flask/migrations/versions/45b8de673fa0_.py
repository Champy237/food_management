"""empty message

Revision ID: 45b8de673fa0
Revises: a9d2773d6007
Create Date: 2025-05-28 01:16:39.864773

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45b8de673fa0'
down_revision = 'a9d2773d6007'
branch_labels = None
depends_on = None


def upgrade():
    # Ajouter la colonne avec une valeur par défaut temporaire pour éviter l'erreur NOT NULL
    with op.batch_alter_table('utilisateur', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mot_de_passe', sa.String(length=255), nullable=False, server_default='motdepasse_temporaire'))

    # Ensuite, on peut supprimer le server_default si on ne le veut pas à long terme (optionnel)
    op.alter_column('utilisateur', 'mot_de_passe', server_default=None)


def downgrade():
    with op.batch_alter_table('utilisateur', schema=None) as batch_op:
        batch_op.drop_column('mot_de_passe')