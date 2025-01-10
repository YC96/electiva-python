from logging.config import fileConfig
import os
from sqlalchemy import engine_from_config, pool
from alembic import context
from app.products.infrastructure.database.productORM import Base as ProductBase
from app.users.infraestructure.orm.user_orm import Base as UserBase
from app.order.infrastructure.database.orm.order_orm import Base as OrderBase
from app.order.infrastructure.database.orm.order_item_orm import Base as OrderItemBase

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
target_metadata = [
    ProductBase.metadata,
    UserBase.metadata,
    OrderBase.metadata,
    OrderItemBase.metadata,
]

def get_url():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    server = os.getenv("DB_SERVER", "db")
    db = os.getenv("POSTGRES_DB")
    return f"postgresql://{user}:{password}@{server}:5432/{db}"

config.set_main_option("sqlalchemy.url", get_url())

def run_migrations_offline():
    """Run migrations in 'offline' mode.
    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well. By skipping the Engine creation
    we don't even need a DBAPI to be available.
    Calls to context.execute() here emit the given string to the
    script output.
    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode.
    In this scenario we need to create an Engine
    and associate a connection with the context.
    """
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()