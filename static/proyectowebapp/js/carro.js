function updateCart(productId, action) {
    $.ajax({
        url: '/carro/update_cart/',  // Asegúrate de que esta URL sea correcta
        type: 'POST',
        data: {
            'product_id': productId,
            'action': action,
            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        success: function(response) {
            if(response.success) {
                if(action === 'remove' || response.quantity === 0) {
                    $('#product-row-' + productId).remove();
                    $('#summary-item-' + productId).remove();
                } else {
                    $('#quantity-' + productId).text(response.quantity);
                    $('#price-' + productId).text(response.price);
                    $('#product-row-' + productId).find('td:first').text(response.name);
                    $('#summary-item-' + productId).html(response.name + ' <span class="badge bg-primary rounded-pill">' + response.quantity + '</span>');
                }
                
                $('#total-price').text(response.total);
                
                if(response.cart_empty) {
                    $('#cart-body').html('<tr><td colspan="4"><div class="alert alert-info text-center">El carrito está vacío</div></td></tr>');
                    $('#summary-list').empty();
                    $('a[href="/pedidos/checkout/"]').hide();
                } else {
                    $('a[href="/pedidos/checkout/"]').show();
                }
            } else {
                alert('Error al actualizar el carrito: ' + response.error);
            }
        },
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
            alert('Error al actualizar el carrito');
        }
    });
}
