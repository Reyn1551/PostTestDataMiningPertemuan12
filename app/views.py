from app import app, render_template, request
import json

MENU_MAKANAN = {
    "Sushi Salmon": 45000,
    "Sushi Tuna": 42000,
    "Sashimi Salmon": 55000,
    "Ramen Ayam": 35000,
    "Ramen Sapi": 40000,
    "Takoyaki": 25000,
    "Udon Tempura": 45000,
    "Katsu Curry": 50000
}

MENU_MINUMAN = {
    "Ocha (Panas/Dingin)": 10000,
    "Matcha Latte": 25000,
    "Es Jeruk Nipis": 15000,
    "Sake (Non-Alkohol)": 30000,
    "Air Mineral": 8000,
    "Cola": 12000,
    "Melon Soda": 20000,
    "Lemon Tea": 15000
}

@app.route("/")
def index():
    return render_template('utama.html', makanan=MENU_MAKANAN, minuman=MENU_MINUMAN)

@app.route('/bayar', methods=['POST'])
def bayar():
    nama_pelanggan = request.form.get('pemesan')
    cart_data_raw = request.form.get('cart_data')
    
    cart_items = []
    grand_total = 0
    
    if cart_data_raw:
        try:
            cart_data = json.loads(cart_data_raw)
            for item in cart_data:
                nama = item.get('name')
                qty = int(item.get('qty'))
                price = MENU_MAKANAN.get(nama) or MENU_MINUMAN.get(nama) or int(item.get('price'))
                
                subtotal = price * qty
                grand_total += subtotal
                
                cart_items.append({
                    'name': nama,
                    'price': price,
                    'qty': qty,
                    'subtotal': subtotal
                })
        except ValueError:
            pass 

    return render_template('result.html', 
                           pemesan=nama_pelanggan, 
                           items=cart_items, 
                           total=grand_total)

if __name__ == '__main__':
    app.run(debug=True)