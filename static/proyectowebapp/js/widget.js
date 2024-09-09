function updateCart(productId, action) {
    $.ajax({
        url: '/carro/update_cart/',  
        type: 'POST',
        data: {
            'product_id': productId,
            'action': action,
            'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        success: function(response) {
            if(response.success) {
                $('#quantity-' + productId).text(response.quantity);
                $('#price-' + productId).text(response.price + ' ₲');
                $('#total-price').text(response.total);
                
                if(response.quantity === 0) {
                    $('#product-row-' + productId).fadeOut(300, function() { $(this).remove(); });
                }
                
                if(response.cart_empty) {
                    $('#cart-body').html('<tr><td colspan="3"><div class="alert alert-danger text-center mb-0">Sin productos</div></td></tr>');
                    $('.card-footer').html('<a href="/tienda/" class="btn btn-primary"><i class="fas fa-store me-2"></i>Ir a la Tienda</a>');
                }
            }
        },
        error: function(xhr, errmsg, err) {
            console.log(xhr.status + ": " + xhr.responseText);
            alert('Error al actualizar el carrito');
        }
    });
}