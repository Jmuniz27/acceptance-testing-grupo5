from behave import given, when, then
from inventory import (
    create_inventory,
    add_product,
    find_product,
    list_products,
    update_quantity,
    format_inventory,
)


# Escenario 1: Add a product

@given('the inventory is empty')
def step_impl(context):
    context.inventory = create_inventory()


@when('the user adds a product "{product}"')
def step_impl(context, product):
    # Valores por defecto porque el escenario solo especifica el nombre
    add_product(context.inventory, product, quantity=1, category="General", price=0.0)


@then('the inventory should contain "{product}"')
def step_impl(context, product):
    assert find_product(context.inventory, product) is not None, \
        f'Product "{product}" not found in the inventory'


# Escenario 2: List all products

@given('the inventory contains products:')
def step_impl(context):
    context.inventory = create_inventory()
    has_quantity = "Quantity" in context.table.headings
    for row in context.table:
        quantity = int(row["Quantity"]) if has_quantity else 1
        add_product(context.inventory, row["Product"], quantity=quantity,
                    category="General", price=0.0)


@when('the user lists all products')
def step_impl(context):
    context.output = format_inventory(list_products(context.inventory))


@then('the output should contain:')
def step_impl(context):
    expected = context.text.strip()
    assert expected in context.output, f'Expected:\n{expected}\nGot:\n{context.output}'


# Escenario 3: Update quantity

@when('the user updates product "{product}" to quantity "{quantity}"')
def step_impl(context, product, quantity):
    update_quantity(context.inventory, product, int(quantity))


@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_impl(context, product, quantity):
    found = find_product(context.inventory, product)
    assert found is not None, f'Product "{product}" not found in the inventory'
    assert str(found["quantity"]) == quantity, \
        f'Expected quantity "{quantity}" but got "{found["quantity"]}"'
