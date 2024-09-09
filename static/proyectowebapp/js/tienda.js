$(document).ready(function() {
    $('.add-to-cart').click(function(e) {
        e.preventDefault();
        var productId = $(this).data('product-id');
        var button = $(this);
        button.prop('disabled', true).html('<i class="fas fa-spinner fa-spin me-2"></i>Agregando...');
        
        $.ajax({
            url: '/carro/update_cart/',  // Asegúrate de que esta URL sea correcta
            type: 'POST',
            data: {
                'product_id': productId,
                'action': 'add',
                'csrfmiddlewaretoken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            success: function(response) {
                if(response.success) {
                    $('#cart-widget').load(location.href + ' #cart-widget>*', '', function() {
                        button.prop('disabled', false).html('<i class="fas fa-check me-2"></i>Agregado');
                        setTimeout(function() {
                            button.html('<i class="fas fa-cart-plus me-2"></i>Agregar al carrito');
                        }, 2000);
                    });
                } else {
                    alert('Error al añadir el producto: ' + response.error);
                    button.prop('disabled', false).html('<i class="fas fa-cart-plus me-2"></i>Agregar al carrito');
                }
            },
            error: function(xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
                alert('Error al añadir el producto al carrito');
                button.prop('disabled', false).html('<i class="fas fa-cart-plus me-2"></i>Agregar al carrito');
            }
        });
    });
});