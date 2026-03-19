import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'D:/Real OneDrive/OneDrive/00 STRONGBOW/Second Brain/house-pics/detail.html'

def fmt_vnd(n):
    return '{:,}'.format(n) + 'đ'

def sub_item(label, price, spec=''):
    spec_html = f'<span class="text-gray-400 text-xs block">{spec}</span>' if spec else ''
    return f'''          <div class="sub-row flex items-start gap-2 py-1 pl-4 border-l-2 border-gray-100 ml-2">
            <span class="flex-1 text-gray-600 text-xs">{label}{spec_html}</span>
            <span class="text-gray-500 text-xs tabular-nums shrink-0">{fmt_vnd(price)}</span>
          </div>'''

def item_row(label, price, section, must=False, spec='', children=''):
    sc = 'state-must' if must else 'state-keep'
    btn = '<span class="btn-must-pill">Bắt buộc</span>' if must else '<button class="btn-toggle btn-keep" onclick="cycleState(this)">Giữ</button>'
    disc = '' if must else '''
            <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>'''
    spec_html = f'<span class="text-gray-400 text-xs block mt-0.5">{spec}</span>' if spec else ''
    children_html = f'\n{children}' if children else ''
    return f'''        <div class="item-row {sc}" data-price="{price}" data-section="{section}" data-state="keep" data-disc="0">
          <div class="flex items-center gap-2">
            {btn}
            <span class="flex-1 font-medium text-sm">{label}{spec_html}</span>
            <span class="price-val tabular-nums font-semibold text-sm shrink-0">{fmt_vnd(price)}</span>
          </div>{disc}{children_html}
        </div>'''

def section_card(title, sec_id, subtitle, color, items_html, total_id, share_id=''):
    if share_id:
        right = f'<span class="ml-auto text-xs font-semibold text-gray-400">÷3: <span class="text-amber-700 font-bold" id="{share_id}">...</span></span>'
    else:
        right = f'<span class="ml-auto text-base font-bold text-amber-700" id="{total_id}-hdr">...</span>'
    return f'''
    <section>
      <div class="flex items-center gap-3 mb-2">
        <div class="w-1 h-7 {color} rounded"></div>
        <div class="flex-1 min-w-0">
          <h2 class="text-sm font-bold">{title}</h2>
          <p class="text-xs text-gray-400">{subtitle}</p>
        </div>
        {right}
      </div>
      <div class="bg-white rounded-2xl shadow-sm border border-gray-100 p-4 space-y-1">
{items_html}
        <div class="border-t pt-2 mt-2">
          <div class="flex justify-between text-xs font-bold text-amber-700"><span>Tổng mục</span><span id="{total_id}" class="tabular-nums">...</span></div>
        </div>
      </div>
    </section>'''

# ── I. PHÁ DỠ T2 ──
phadot2_html = '\n'.join([
    item_row('Tháo dỡ cửa gỗ cửa chính', 1200000, 'phadot2', must=True, spec='bộ ×1'),
    item_row('Tháo dỡ hệ tủ bếp cũ', 2400000, 'phadot2', must=True, spec='tủ bếp + kính ốp bếp + gạch men ốp tường cũ'),
    item_row('Tháo dỡ hệ tủ trang trí phòng khách', 360000, 'phadot2', must=True),
    item_row('Cắt + phá dỡ bậu tường cửa liền vách 1000×600mm', 480000, 'phadot2', must=True),
    item_row('Cắt đục chân tường cửa', 300000, 'phadot2', must=True),
    item_row('Ốp gạch thẻ bếp (nhân công + vật tư phụ)', 900000, 'phadot2', must=True),
])
sec1 = section_card('Tầng 2 — Phá Dỡ', 'phadot2', 'Dùng chung ÷3 · Bắt buộc', 'bg-gray-400', phadot2_html, 'phadot2-total', 'phadot2-share')

# ── II. WC THÔ T3 ──
thot3_html = '\n'.join([
    item_row('Tháo dỡ thiết bị vệ sinh cũ', 360000, 'thot3', must=True),
    item_row('Dóc vữa và gạch ốp lát sàn/tường WC cũ', 3225000, 'thot3', must=True, spec='17.9 m²'),
    item_row('Trát + láng lại tường vệ sinh', 5370000, 'thot3', must=True, spec='17.9 m² · vật tư + nhân công'),
    item_row('Trát cầm cạnh cửa', 673200, 'thot3', must=True),
    item_row('Vật tư gạch ốp lát', 6616000, 'thot3', must=True, spec='19.69 m² × 336k · thanh toán theo hóa đơn'),
    item_row('Chống thấm Sika (2 thành phần)', 4200000, 'thot3', must=True, spec='Cổ ống + quét mặt sàn'),
    item_row('Ốp + lát gạch (nhân công + vật tư phụ)', 5370000, 'thot3', must=True, spec='17.9 m²'),
])
sec2 = section_card('Tầng 3 — WC Thô', 'thot3', 'T3 tự trả · Bắt buộc', 'bg-amber-500', thot3_html, 'thot3-total')

# ── III. WC THÔ T4 ──
thot4_html = '\n'.join([
    item_row('Tháo dỡ thiết bị vệ sinh cũ', 360000, 'thot4', must=True),
    item_row('Tháo dỡ cửa cũ', 480000, 'thot4', must=True, spec='2 bộ'),
    item_row('Dóc vữa và gạch ốp lát sàn/tường WC cũ', 3225000, 'thot4', must=True, spec='17.9 m²'),
    item_row('Xây két xí âm vệ sinh', 960000, 'thot4', must=True),
    item_row('Vật tư gạch ốp lát tiêu chuẩn', 7160000, 'thot4', must=True, spec='17.9 m² × 400k'),
    item_row('Vật tư gạch giả thẻ 400×800', 4157000, 'thot4', must=True, spec='8.66 m² × 480k'),
    item_row('Trát + láng lại tường vệ sinh', 5370000, 'thot4', must=True, spec='17.9 m²'),
    item_row('Trát cầm cạnh cửa', 675000, 'thot4', must=True),
    item_row('Chống thấm Sika (2 thành phần)', 4200000, 'thot4', must=True),
    item_row('Ốp + lát gạch tiêu chuẩn (nhân công)', 6367200, 'thot4', must=True, spec='18.95 m² × 336k'),
    item_row('Ốp gạch thẻ điểm nhấn (nhân công)', 2400000, 'thot4', must=True),
])
sec3 = section_card('Tầng 4 — WC Thô', 'thot4', 'T4 tự trả · Bắt buộc', 'bg-gray-500', thot4_html, 'thot4-total')

# ── IV. MEP ──
mep_html = '\n'.join([
    item_row('Nhân công lắp điện toàn nhà', 10800000, 'mep', must=True, spec='WC T3+T4 + bếp T2 + phòng ngủ T4'),
    item_row('Vật tư điện thô (tạm tính)', 9600000, 'mep', must=True, spec='Dây Trần Phú, ổ cắm Panasonic — CĐT có thể tự cung cấp'),
    item_row('Nhân công cấp thoát nước WC T3+T4 + bếp', 11400000, 'mep', must=True, spec='2.5 khu × 4,560k'),
    item_row('Nhân công đấu nối xí bệt treo tường T4', 1800000, 'mep', must=True),
    item_row('Vật tư ống nước + phụ kiện', 12000000, 'mep', must=True, spec='2.5 khu × 4,800k · không bao gồm thiết bị đầu cuối'),
])
sec4 = section_card('Điện Nước (MEP)', 'mep', 'Dùng chung ÷3 · Bắt buộc', 'bg-blue-400', mep_html, 'mep-total', 'mep-share')

# ── V. THẠCH CAO + SƠN ──
thaoson_html = '\n'.join([
    item_row('Trần thạch cao thường (P.ngủ T4 + hành lang T2,T4)', 4105500, 'thaoson', spec='13.69 m² · Gyproc Thái Lan 9mm · khung Vĩnh Tường'),
    item_row('Trần thạch cao chống ẩm WC T3+T4', 360000, 'thaoson', spec='Gyproc chống ẩm 9mm'),
    item_row('Tấm thăm trần chống ẩm 45×45cm (WC T3+T4)', 840000, 'thaoson', spec='2 cái × 420k'),
    item_row('Thanh nẹp Z trần WC T3+T4', 806400, 'thaoson', spec='13.44m'),
    item_row('Sơn bả trần thạch cao', 3457000, 'thaoson', spec='28.8 m² · Dulux EasyClean'),
    item_row('Sơn lại tường trong nhà', 9000000, 'thaoson', spec='100 m² (tạm tính) · Dulux EasyClean'),
])
sec5 = section_card('Thạch Cao + Sơn', 'thaoson', 'Dùng chung ÷3', 'bg-purple-400', thaoson_html, 'thaoson-total', 'thaoson-share')

# ── VI. NHÔM KÍNH ──
nhomkinh_html = '\n'.join([
    item_row('Cửa lùa hệ Slim 4 cánh — phòng khách T2', 25614000, 'nk_shared', spec='5.54m × 4,625k · Nhôm Slim 1.6mm + kính cường lực 8mm · Giai đoạn 2'),
    item_row('Phụ kiện cửa lùa (ray, bộ trượt, tay nắm âm)', 5400000, 'nk_shared', spec='Draho, Kinlong · Giai đoạn 2'),
    item_row('Cửa WC T3 composite 700×2200mm', 5400000, 'nk_t3', spec='WPC 40mm · chống nước, chống mối mọt · gioăng giảm chấn + 3 bản lề'),
    item_row('Cửa WC T4 composite 700×2200mm', 5400000, 'nk_t4', spec='WPC 40mm · chống nước, chống mối mọt'),
    item_row('Cửa phòng ngủ T4 composite 850×2200mm', 5760000, 'nk_t4', spec='WPC 40mm'),
])
sec6 = section_card('Nhôm Kính', 'nhomkinh', 'Cửa lùa ÷3 · Cửa WC/phòng ngủ T3/T4 tự trả', 'bg-cyan-400', nhomkinh_html, 'nhomkinh-total')

# ── VII. PHÒNG KHÁCH ──
pk_ketivi = '\n'.join([
    sub_item('Kệ tivi MDF melamine Thái Lan', 5400000, '2.5m × 0.33 × 0.38'),
    sub_item('Ray ngăn kéo eurogold', 576000, '4 bộ × 144k'),
])
pk_beca = '\n'.join([
    sub_item('Tủ MDF melamine Thái Lan', 3600000, '0.65×0.35×0.68'),
    sub_item('Bản lề giảm chấn Blum', 144000, '4 cái × 36k'),
])
pk_html = '\n'.join([
    item_row('Kệ tivi', 5976000, 'pk', children=pk_ketivi),
    item_row('Vách ốp tivi', 8799000, 'pk', spec='Vách phẳng + nan gỗ MDF melamine · 6.67 m²'),
    item_row('Tủ đặt bể cá', 3744000, 'pk', children=pk_beca),
])
sec7 = section_card('Phòng Khách T2', 'pk', 'Dùng chung ÷3', 'bg-amber-400', pk_html, 'pk-total', 'pk-share')

# ── VIII. PHÒNG BẾP ──
bep_duoi = '\n'.join([
    sub_item('Tủ bếp dưới MDF melamine', 8286000, '3m × 0.6 × 0.85 · thùng chậu rửa bọc picomat'),
    sub_item('Bản lề giảm chấn Kithome', 324000, '6 cái × 54k'),
    sub_item('Ray ngăn kéo eurogold', 144000, '1 bộ × 144k'),
    sub_item('Đá mặt bếp thạch anh nhân tạo', 756000, '3md × 252k'),
])
bep_tren = '\n'.join([
    sub_item('Tủ bếp trên MDF + laminate kim loại', 7610000, '3.25m × 0.35 × 1.25'),
    sub_item('Bản lề giảm chấn Kithome', 1080000, '20 cái × 54k'),
    sub_item('Pittong trợ lực eurogold', 504000, '6 cái × 84k'),
    sub_item('Đèn LED thanh nhôm', 756000, '3.5md × 216k'),
    sub_item('Nguồn chuyển 220v→12v', 180000, '1 cái'),
    sub_item('Cảm biến vẫy/chạm', 180000, '1 cái'),
])
bep_tulanh = '\n'.join([
    sub_item('Tủ lạnh MDF melamine', 3455000, '0.69×0.6×2.7 = 1.86 m²'),
    sub_item('Bản lề giảm chấn Kithome', 216000, '4 cái × 54k'),
])
bep_html = '\n'.join([
    item_row('Tủ bếp dưới + đá mặt bếp', 9510000, 'bep', children=bep_duoi),
    item_row('Tủ bếp trên', 10310000, 'bep', children=bep_tren),
    item_row('Hệ tủ lạnh', 3671000, 'bep', children=bep_tulanh),
])
sec8 = section_card('Phòng Bếp T2', 'bep', 'Dùng chung ÷3', 'bg-orange-400', bep_html, 'bep-total', 'bep-share')

# ── IX. WC FIXTURES (T3 + T4) ──
def wc_fix(sec):
    return '\n'.join([
        item_row('Đèn trần WC', 2028000, sec, spec='13 bộ × 156k'),
        item_row('Kệ tủ nhỏ trên bồn cầu', 2268000, sec, spec='0.54 m² × 4,200k'),
        item_row('Tủ trên bồn cầu', 7560000, sec, spec='1.8 m² × 4,200k'),
        item_row('Phụ kiện vệ sinh', 7200000, sec, spec='CĐT chọn nhà cung cấp'),
        item_row('Bồn cầu âm tường DeMuhler ML361001', 9500000, sec, spec='CĐT chọn nhà cung cấp'),
        item_row('Chậu rửa INAX L-333V bán âm', 2500000, sec, spec='CĐT chọn nhà cung cấp'),
        item_row('Bình nóng lạnh 20L Rossi', 2148000, sec, spec='CĐT chọn nhà cung cấp'),
    ])
sec9  = section_card('WC T3 — Thiết Bị & Nội Thất', 'wc3fix', 'T3 tự trả', 'bg-amber-400', wc_fix('wc3fix'), 'wc3fix-total')
sec10 = section_card('WC T4 — Thiết Bị & Nội Thất', 'wc4fix', 'T4 tự trả', 'bg-gray-400', wc_fix('wc4fix'), 'wc4fix-total')

# ── X. PHÒNG NGỦ T4 ──
ng_vach = '\n'.join([
    sub_item('Vách ốp phẳng MDF melamine', 8687000, '7.62 m²'),
    sub_item('Vách nan gỗ MDF melamine', 2852000, '2.16 m²'),
])
ng_tua = '\n'.join([
    sub_item('Tủ quần áo MDF cánh pano melamine', 10549000, '1.6×0.5×2.68 = 4.29 m²'),
    sub_item('Tay nắm hợp kim vàng bóng', 576000, '8 cái × 72k'),
    sub_item('Bản lề giảm chấn Blum', 1008000, '28 cái × 36k'),
    sub_item('Pittong trợ lực eurogold', 384000, '4 cái × 96k'),
    sub_item('Đèn LED thanh nhôm', 324000, '1.5md × 216k'),
    sub_item('Nguồn chuyển 220v→12v', 180000, '1 cái'),
    sub_item('Cảm biến vẫy/chạm', 180000, '1 cái'),
])
ng_tivi = '\n'.join([
    sub_item('Hệ tủ tivi + trang trí + bàn phấn MDF', 20768000, '3.15×0.45×2.68 = 8.44 m²'),
    sub_item('Tay nắm hợp kim vàng bóng', 936000, '13 cái × 72k'),
    sub_item('Bản lề giảm chấn Blum', 972000, '27 cái × 36k'),
    sub_item('Ray ngăn kéo eurogold', 576000, '4 bộ × 144k'),
    sub_item('Pittong trợ lực eurogold', 192000, '2 cái × 96k'),
    sub_item('Đèn LED thanh nhôm', 1577000, '7.3md'),
    sub_item('Nguồn chuyển 220v→12v', 180000, '1 cái'),
    sub_item('Cảm biến vẫy/chạm', 180000, '1 cái'),
])
ng_html = '\n'.join([
    item_row('Vách ốp đầu giường', 11539000, 'ng', children=ng_vach),
    item_row('Tủ quần áo', 12841000, 'ng', children=ng_tua),
    item_row('Hệ tủ tivi + trang trí + bàn phấn', 25381000, 'ng', children=ng_tivi),
    item_row('Gương LED (0.8×0.9m, viền gỗ MDF)', 4200000, 'ng'),
    item_row('Vận chuyển nội thất', 3600000, 'ng'),
])
sec11 = section_card('Phòng Ngủ T4', 'ng', 'T4 tự trả', 'bg-gray-500', ng_html, 'ng-total')

# ── XI. PHẦN KHÁC ──
khac_html = item_row('Sàn gỗ nhựa phòng ngủ T4', 2496000, 'khac', spec='13 m² × 192k')
sec12 = section_card('Phần Khác', 'khac', 'T4 tự trả', 'bg-gray-400', khac_html, 'khac-total')

# ── XII. PHÍ THIẾT KẾ ──
thietke_html = item_row('Phí thiết kế nội thất (sau giảm 30%)', 13629000, 'thietke', must=True)
sec13 = section_card('Phí Thiết Kế', 'thietke', 'Dùng chung ÷3 · Bắt buộc', 'bg-rose-400', thietke_html, 'thietke-total', 'thietke-share')

html = '''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Báo Giá Chi Tiết — Nhà Anh Huy</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet" />
  <style>
    body { font-family: "Inter", sans-serif; }
    .item-row { transition: opacity .2s; padding: 5px 0; }
    .item-row.cut { opacity:.4; }
    .btn-toggle { cursor:pointer; border-radius:9999px; font-size:11px; font-weight:600; padding:2px 9px; border:1.5px solid; transition:all .15s; user-select:none; white-space:nowrap; flex-shrink:0; }
    .btn-keep  { background:#dcfce7; color:#166534; border-color:#86efac; }
    .btn-cut   { background:#fee2e2; color:#991b1b; border-color:#fca5a5; }
    .btn-buy   { background:#dbeafe; color:#1e40af; border-color:#93c5fd; }
    .btn-must-pill { font-size:10px; font-weight:700; padding:2px 8px; border-radius:9999px; background:#fef9c3; color:#854d0e; border:1.5px solid #fde047; white-space:nowrap; flex-shrink:0; }
    .state-keep .price-val { color:#166534; }
    .state-cut  .price-val { color:#9ca3af; text-decoration:line-through; }
    .state-buy  .price-val { color:#1e40af; }
    .disc-row { display:none; margin-top:3px; padding-left:2px; gap:4px; flex-wrap:wrap; align-items:center; }
    .state-buy .disc-row { display:flex; }
    .disc-pill { cursor:pointer; font-size:10px; font-weight:700; padding:2px 7px; border-radius:9999px; border:1.5px solid #bfdbfe; background:#eff6ff; color:#1e40af; transition:all .15s; user-select:none; }
    .disc-pill:hover { background:#dbeafe; }
    .disc-pill.active { background:#1e40af; color:#fff; border-color:#1e40af; }
    .disc-orig { font-size:10px; color:#9ca3af; text-decoration:line-through; margin-left:4px; }
    .disc-effective { font-size:10px; color:#1e40af; font-weight:700; margin-left:2px; }
    @keyframes flashGreen { 0%{background:#dcfce7;} 100%{background:transparent;} }
    @keyframes flashRed   { 0%{background:#fee2e2;} 100%{background:transparent;} }
    .flash-green { animation: flashGreen .6s ease-out; }
    .flash-red   { animation: flashRed   .6s ease-out; }
  </style>
</head>
<body class="bg-gray-50 min-h-screen">
  <div class="max-w-2xl mx-auto px-4 py-6 space-y-4">

    <div class="bg-amber-50 border border-amber-200 rounded-2xl p-5">
      <div class="flex items-center justify-between">
        <div>
          <h1 class="text-xl font-bold text-amber-900">Báo Giá Chi Tiết</h1>
          <p class="text-sm text-amber-700 mt-0.5">Tất cả hạng mục · Có thể toggle từng dòng</p>
        </div>
        <a href="index.html" class="text-xs text-amber-600 underline">← Xem bản gia đình</a>
      </div>
    </div>

''' + sec1 + sec2 + sec3 + sec4 + sec5 + sec6 + sec7 + sec8 + sec9 + sec10 + sec11 + sec12 + sec13 + '''

    <!-- Summary -->
    <section>
      <div class="flex items-center gap-3 mb-2">
        <div class="w-1 h-7 bg-gray-800 rounded"></div>
        <h2 class="text-sm font-bold">Tổng kết</h2>
      </div>
      <div class="grid sm:grid-cols-3 gap-3 mb-3">
        <div class="bg-white rounded-2xl border-2 border-amber-400 p-4">
          <p class="text-xs font-bold text-amber-600 uppercase mb-1">T3</p>
          <p class="text-2xl font-bold mb-2" id="summary-t3">...</p>
          <div class="space-y-0.5 text-xs text-gray-400" id="summary-t3-bd"></div>
        </div>
        <div class="bg-white rounded-2xl border border-gray-100 p-4">
          <p class="text-xs font-bold text-gray-400 uppercase mb-1">T4</p>
          <p class="text-2xl font-bold mb-2" id="summary-t4">...</p>
          <div class="space-y-0.5 text-xs text-gray-400" id="summary-t4-bd"></div>
        </div>
        <div class="bg-white rounded-2xl border border-gray-100 p-4">
          <p class="text-xs font-bold text-gray-400 uppercase mb-1">T2</p>
          <p class="text-2xl font-bold mb-2" id="summary-t2">...</p>
          <p class="text-xs text-gray-400">Phần chung ÷3</p>
        </div>
      </div>
      <div class="bg-gray-900 text-white rounded-2xl p-5">
        <p class="text-xs text-gray-400 mb-1">Grand Total</p>
        <p class="text-3xl font-bold" id="grand-total">...</p>
      </div>
    </section>

    <!-- Save/Load -->
    <section class="bg-white border border-gray-200 rounded-2xl p-4">
      <h3 class="font-bold text-gray-800 mb-3 text-sm">Lưu / Tải trạng thái</h3>
      <div class="flex gap-2">
        <button onclick="saveJSON()" class="cursor-pointer bg-blue-600 hover:bg-blue-700 text-white text-sm font-semibold px-4 py-2 rounded-xl">Lưu JSON</button>
        <label class="cursor-pointer bg-blue-50 hover:bg-blue-100 text-blue-700 border border-blue-200 text-sm font-semibold px-4 py-2 rounded-xl">
          Tải JSON<input type="file" accept=".json" onchange="loadJSON(event)" class="hidden" />
        </label>
      </div>
    </section>

  </div>

  <script>
    const fmt = n => Math.round(n).toLocaleString("vi-VN") + "đ";
    const prevVals = {};

    function setText(id, val, numeric) {
      const el = document.getElementById(id);
      if (!el) return;
      const prev = prevVals[id];
      prevVals[id] = numeric;
      el.textContent = val;
      el.classList.remove("flash-green","flash-red");
      void el.offsetWidth;
      if (prev !== undefined && numeric !== undefined && numeric !== prev)
        el.classList.add(numeric < prev ? "flash-green" : "flash-red");
    }

    function cycleState(btn) {
      const row = btn.closest(".item-row");
      const states = ["keep","buy","cut"];
      const labels = ["Giữ","Tự mua","Cắt"];
      const cls    = ["btn-keep","btn-buy","btn-cut"];
      let idx = states.indexOf(row.dataset.state);
      idx = (idx + 1) % 3;
      row.dataset.state = states[idx];
      row.className = row.className.replace(/state-\\w+/, "state-" + states[idx]);
      btn.className = btn.className.replace(/btn-\\w+/, cls[idx]);
      btn.textContent = labels[idx];
      if (states[idx] !== "buy") {
        row.dataset.disc = "0";
        row.querySelectorAll(".disc-pill").forEach(p => p.classList.remove("active"));
        const o = row.querySelector(".disc-orig"), e = row.querySelector(".disc-effective");
        if (o) o.textContent = ""; if (e) e.textContent = "";
        const pv = row.querySelector(".price-val");
        if (pv) pv.textContent = fmt(+row.dataset.price);
      }
      recalc();
    }

    function setDisc(pill, pct) {
      const row = pill.closest(".item-row");
      const base = +row.dataset.price;
      const cur  = +row.dataset.disc;
      if (cur === pct) { pct = 0; pill.classList.remove("active"); }
      else { row.querySelectorAll(".disc-pill").forEach(p => p.classList.remove("active")); pill.classList.add("active"); }
      row.dataset.disc = pct;
      const eff = base * (1 - pct/100);
      const pv = row.querySelector(".price-val"), o = row.querySelector(".disc-orig"), e = row.querySelector(".disc-effective");
      if (pct > 0) {
        if (pv) pv.textContent = fmt(eff);
        if (o)  o.textContent  = fmt(base);
        if (e)  e.textContent  = "-" + pct + "%";
      } else {
        if (pv) pv.textContent = fmt(base);
        if (o)  o.textContent  = "";
        if (e)  e.textContent  = "";
      }
      recalc();
    }

    function sectionTotal(sec) {
      let t = 0;
      document.querySelectorAll(`[data-section="${sec}"]`).forEach(row => {
        if (row.dataset.state === "cut") return;
        t += +row.dataset.price * (1 - (+row.dataset.disc||0)/100);
      });
      return t;
    }

    function recalc() {
      const phadot2 = sectionTotal("phadot2");
      const mep     = sectionTotal("mep");
      const thaoson = sectionTotal("thaoson");
      const nk_sh   = sectionTotal("nk_shared");
      const pk      = sectionTotal("pk");
      const bep     = sectionTotal("bep");
      const thietke = sectionTotal("thietke");
      const shared  = phadot2 + mep + thaoson + nk_sh + pk + bep + thietke;
      const per3    = shared / 3;

      const thot3  = sectionTotal("thot3");
      const nk_t3  = sectionTotal("nk_t3");
      const wc3fix = sectionTotal("wc3fix");
      const t3     = thot3 + nk_t3 + wc3fix + per3;

      const thot4  = sectionTotal("thot4");
      const nk_t4  = sectionTotal("nk_t4");
      const wc4fix = sectionTotal("wc4fix");
      const ng     = sectionTotal("ng");
      const khac   = sectionTotal("khac");
      const t4     = thot4 + nk_t4 + wc4fix + ng + khac + per3;

      // Section totals
      setText("phadot2-total", fmt(phadot2), phadot2); setText("phadot2-share", fmt(phadot2/3), phadot2/3);
      setText("thot3-total",   fmt(thot3), thot3);
      setText("thot4-total",   fmt(thot4), thot4);
      setText("mep-total",     fmt(mep), mep);     setText("mep-share", fmt(mep/3), mep/3);
      setText("thaoson-total", fmt(thaoson), thaoson); setText("thaoson-share", fmt(thaoson/3), thaoson/3);
      const nk_all = nk_sh + nk_t3 + nk_t4;
      setText("nhomkinh-total", fmt(nk_all), nk_all);
      setText("pk-total",  fmt(pk), pk);   setText("pk-share",  fmt(pk/3), pk/3);
      setText("bep-total", fmt(bep), bep); setText("bep-share", fmt(bep/3), bep/3);
      setText("wc3fix-total", fmt(wc3fix), wc3fix);
      setText("wc4fix-total", fmt(wc4fix), wc4fix);
      setText("ng-total",    fmt(ng), ng);
      setText("khac-total",  fmt(khac), khac);
      setText("thietke-total", fmt(thietke), thietke); setText("thietke-share", fmt(thietke/3), thietke/3);

      setText("summary-t3", fmt(t3), t3);
      setText("summary-t4", fmt(t4), t4);
      setText("summary-t2", fmt(per3), per3);

      document.getElementById("summary-t3-bd").innerHTML =
        `<div class="flex justify-between"><span>WC thô</span><span>${fmt(thot3)}</span></div>
         <div class="flex justify-between"><span>Cửa WC T3</span><span>${fmt(nk_t3)}</span></div>
         <div class="flex justify-between"><span>WC thiết bị</span><span>${fmt(wc3fix)}</span></div>
         <div class="flex justify-between"><span>Phần chung ÷3</span><span>${fmt(per3)}</span></div>`;

      document.getElementById("summary-t4-bd").innerHTML =
        `<div class="flex justify-between"><span>WC thô</span><span>${fmt(thot4)}</span></div>
         <div class="flex justify-between"><span>Cửa WC+P.ngủ T4</span><span>${fmt(nk_t4)}</span></div>
         <div class="flex justify-between"><span>WC thiết bị</span><span>${fmt(wc4fix)}</span></div>
         <div class="flex justify-between"><span>Phòng ngủ + khác</span><span>${fmt(ng+khac)}</span></div>
         <div class="flex justify-between"><span>Phần chung ÷3</span><span>${fmt(per3)}</span></div>`;

      setText("grand-total", fmt(t3 + t4 + per3), t3 + t4 + per3);
    }

    function saveJSON() {
      const state = {};
      document.querySelectorAll(".item-row[data-section]").forEach((row, i) => {
        state[(row.dataset.section||"x")+"_"+i] = {state: row.dataset.state, disc: row.dataset.disc};
      });
      const a = document.createElement("a");
      a.href = "data:application/json," + encodeURIComponent(JSON.stringify(state, null, 2));
      a.download = "bao-gia-detail.json"; a.click();
    }

    function loadJSON(event) {
      const file = event.target.files[0]; if (!file) return;
      const reader = new FileReader();
      reader.onload = e => {
        try {
          const state = JSON.parse(e.target.result);
          const rows = document.querySelectorAll(".item-row[data-section]");
          rows.forEach((row, i) => {
            const d = state[(row.dataset.section||"x")+"_"+i]; if (!d) return;
            const labels = {keep:"Giữ", buy:"Tự mua", cut:"Cắt"};
            const cls    = {keep:"btn-keep", buy:"btn-buy", cut:"btn-cut"};
            row.dataset.state = d.state;
            row.className = row.className.replace(/state-\\w+/, "state-"+d.state);
            const btn = row.querySelector(".btn-toggle");
            if (btn) { btn.className = btn.className.replace(/btn-\\w+/, cls[d.state]); btn.textContent = labels[d.state]; }
            row.dataset.disc = d.disc;
            if (+d.disc > 0) {
              const pill = row.querySelector(`.disc-pill[onclick*="${d.disc}"]`);
              if (pill) pill.classList.add("active");
              const pv = row.querySelector(".price-val");
              if (pv) pv.textContent = fmt(+row.dataset.price * (1 - d.disc/100));
            }
          });
          recalc();
        } catch(err) { alert("Lỗi đọc file JSON"); }
      };
      reader.readAsText(file);
    }

    window.addEventListener("DOMContentLoaded", recalc);
  </script>
</body>
</html>'''

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Written:', len(html), 'bytes')
print('Sections:', html.count('data-section='))
