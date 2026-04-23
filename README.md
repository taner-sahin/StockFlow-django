📦 StockFlow

Gerçek dünya e-ticaret sistemlerinde kullanılan stok yönetimi, sipariş akışı ve veritabanı tabanlı sepet mimarisini uygulamak amacıyla geliştirilmiş, backend odaklı bir Django projesidir.

🧠 Hakkında

StockFlow, bir e-ticaret sisteminin en kritik katmanı olan stok kontrolünü ele alır.

Bu projede:

Sepet → Sipariş → Stok düşme akışı
Aynı üründen fazla eklemeyi engelleme
Sipariş sonrası stok güncelleme
Kullanıcı bazlı veri yönetimi

tamamen backend mantığıyla ele alınmıştır.

⚙️ Temel Özellikler
Kimlik doğrulama sistemi (Login / Register / Logout)
Dinamik navbar (kategori + sepet + sipariş sayısı)
Dinamik ana sayfa
Kategori bazlı ürün filtreleme
Ürün detay sayfası (slug yapısı)
🛒 Cart Sistemi (DB Tabanlı)
Veritabanı tabanlı cart yapısı
Sepete ekleme / artırma / azaltma / silme
Aynı ürün tekrar eklenmez → miktar artar
Kullanıcı bazlı sepet yönetimi
Navbar’da dinamik cart count
📦 Order Sistemi
Order modeli
OrderItem modeli
Snapshot mantığı (ürün adı ve fiyatı saklanır)
Checkout (cart → order dönüşümü)
Sipariş sonrası cart temizleme
📊 Sipariş Yönetimi
“Siparişlerim” sayfası
Sipariş detay sayfası
Sipariş durumları:
pending
preparing
shipped
delivered
Navbar’da dinamik sipariş sayısı
Sipariş istatistik kartları
🔥 Backend Özelliklerinden Öne Çıkanlar
Stok kontrolü cart seviyesinde yapılır
Ürün stoktan fazla sepete eklenemez
Checkout sırasında stok otomatik düşer
Sepet ve sipariş işlemleri sadece giriş yapan kullanıcıya açıktır
Kullanıcı sadece kendi siparişlerini görebilir
ID Mantığı
product_id → sepete ekleme
cart_item_id → artır / azalt / sil işlemleri
🔄 Sipariş Akışı
Kullanıcı giriş yapar
Ürün sepete eklenir
Sepet veritabanında tutulur
Kullanıcı checkout yapar
Sipariş oluşturulur
OrderItem’lar oluşturulur (snapshot alınır)
Toplam hesaplanır
Stok düşürülür
Sepet temizlenir
🧱 Teknoloji Yığını
Python
Django
Bootstrap
SQLite
📁 Proje Yapısı
products → ürün listeleme, kategori filtreleme, detay
cart → DB tabanlı sepet sistemi
orders → sipariş oluşturma, checkout, sipariş geçmişi
Template Yapısı
Global templates (base, home)
App bazlı templates
Component mantığı
🎯 Öğrendiklerim
DB tabanlı cart sistemi kurma
Stok kontrolü mantığı
Sipariş akışı tasarlama
Snapshot (anlık veri) mantığı
Backend-first proje geliştirme
Kullanıcı bazlı veri güvenliği
Context processor ile global veri yönetimi
📌 Durum

✅ Backend çekirdeği tamamlandı
✅ Gerçek e-ticaret akışı başarıyla kuruldu

StockFlow projesi, e-ticaret sistemlerinde kritik olan stok yönetimi katmanını başarıyla uygulayan bir backend projesi olarak tamamlanmıştır.

🗺️ Yol Haritası
Proje 1 → StepCart
Proje 2 → OrderCore
Proje 3 → StockFlow ✅
Proje 4 → CouponCart (Kupon Sistemi) ⏳
👨‍💻 Yazar

Taner Şahin
GitHub: https://github.com/TanerSahin19

