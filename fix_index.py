import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

path = 'D:/Real OneDrive/OneDrive/00 STRONGBOW/Second Brain/house-pics/index.html'
with open(path, 'r', encoding='utf-8') as f:
    html = f.read()

# === FIX 1: Move ng items into T4 phong ngu section ===
# Remove stray ng items block from inside thietke section
html = re.sub(
    r'\n      <div class="mt-4 space-y-1\.5 text-sm">.*?</div>\s*</section>(\s*\n\s*<!-- ══.*?TỔNG KẾT)',
    r'\1',
    html, flags=re.DOTALL
)

ng_items_html = '''
      <div class="mt-4 space-y-1.5 text-sm">
            <div class="item-row state-keep" data-price="5760000" data-section="ng" data-state="keep" data-disc="0">
              <div class="flex items-center gap-2">
                <button class="btn-toggle btn-keep" onclick="cycleState(this)">Gi&#x1EEF;</button>
                <span class="flex-1">C&#x1EED;a ph&#xF2;ng ng&#x1EE7; T4</span>
                <span class="price-val tabular-nums font-medium">5,760,000&#x111;</span>
              </div>
              <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>
            </div>
            <div class="item-row state-keep" data-price="11539000" data-section="ng" data-state="keep" data-disc="0">
              <div class="flex items-center gap-2">
                <button class="btn-toggle btn-keep" onclick="cycleState(this)">Gi&#x1EEF;</button>
                <span class="flex-1">V&#xE1;ch &#x1ED1;p &#x111;&#x1EA7;u gi&#x01B0;&#x1EDD;ng</span>
                <span class="price-val tabular-nums font-medium">11,539,000&#x111;</span>
              </div>
              <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>
            </div>
            <div class="item-row state-keep" data-price="12841000" data-section="ng" data-state="keep" data-disc="0">
              <div class="flex items-center gap-2">
                <button class="btn-toggle btn-keep" onclick="cycleState(this)">Gi&#x1EEF;</button>
                <span class="flex-1">T&#x1EE7; qu&#x1EA7;n &#xE1;o</span>
                <span class="price-val tabular-nums font-medium">12,841,000&#x111;</span>
              </div>
              <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>
            </div>
            <div class="item-row state-keep" data-price="25381000" data-section="ng" data-state="keep" data-disc="0">
              <div class="flex items-center gap-2">
                <button class="btn-toggle btn-keep" onclick="cycleState(this)">Gi&#x1EEF;</button>
                <span class="flex-1">H&#x1EC7; t&#x1EE7; tivi + b&#xE0;n ph&#x1EA5;n</span>
                <span class="price-val tabular-nums font-medium">25,381,000&#x111;</span>
              </div>
              <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>
            </div>
            <div class="item-row state-keep" data-price="4200000" data-section="ng" data-state="keep" data-disc="0">
              <div class="flex items-center gap-2">
                <button class="btn-toggle btn-keep" onclick="cycleState(this)">Gi&#x1EEF;</button>
                <span class="flex-1">G&#x1B0;&#x1A1;ng LED</span>
                <span class="price-val tabular-nums font-medium">4,200,000&#x111;</span>
              </div>
              <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>
            </div>
            <div class="item-row state-keep" data-price="3600000" data-section="ng" data-state="keep" data-disc="0">
              <div class="flex items-center gap-2">
                <button class="btn-toggle btn-keep" onclick="cycleState(this)">Gi&#x1EEF;</button>
                <span class="flex-1">V&#x1EAD;n chuy&#x1EC3;n n&#x1ED9;i th&#x1EA5;t</span>
                <span class="price-val tabular-nums font-medium">3,600,000&#x111;</span>
              </div>
              <div class="disc-row"><span class="disc-pill" onclick="setDisc(this,10)">-10%</span><span class="disc-pill" onclick="setDisc(this,20)">-20%</span><span class="disc-pill" onclick="setDisc(this,30)">-30%</span><span class="disc-pill" onclick="setDisc(this,50)">-50%</span><span class="disc-orig"></span><span class="disc-effective"></span></div>
            </div>
        <div class="border-t pt-2 mt-2">
          <div class="flex justify-between text-xs font-bold text-amber-700"><span>T&#x1ED5;ng ph&#xF2;ng ng&#x1EE7; T4</span><span id="ng-total" class="tabular-nums">...</span></div>
        </div>
      </div>'''

# Replace placeholder text in T4 section
old_placeholder = '<p class="mt-3 text-sm text-gray-500">T\u1ee7 tivi + b\xe0n ph\u1ea5n, t\u1ee7 qu\u1ea7n \xe1o, v\xe1ch \u0111\u1ea7u gi\u01b0\u1eddng, gi\u01b0\u1eddng, g\u01b0\u01a1ng LED. T4 t\u1ef1 quy\u1ebft \u0111\u1ecbnh v\xe0 thanh to\xe1n.</p>\n      </div>\n    </section>'
new_placeholder = ng_items_html + '\n      </div>\n    </section>'

if old_placeholder in html:
    html = html.replace(old_placeholder, new_placeholder)
    print('ng items moved into T4 section')
else:
    print('placeholder not found - checking...')
    idx = html.find('T4 t\u1ef1 quy\u1ebft \u0111\u1ecbnh')
    print('placeholder at:', idx)

# === FIX 2: T2 total in recalc ===
if "setText('t2-total'" not in html:
    html = html.replace(
        "setText('t4-total', fmt(t4Total), t4Total);",
        "setText('t4-total', fmt(t4Total), t4Total);\n      setText('t2-total', fmt(sharedPer3), sharedPer3);"
    )
    print('Added t2-total to recalc')

# === FIX 3: Tap hint — clean approach ===
# Remove old broken injection
html = re.sub(r"window\.addEventListener\('DOMContentLoaded', \(\) => \{.*?recalc\(\).*?\}\);",
              "window.addEventListener('DOMContentLoaded', recalc);", html, flags=re.DOTALL)

tap_js = """
    // Tap hint on first toggle button
    window.addEventListener('DOMContentLoaded', function() {
      recalc();
      setTimeout(function() {
        var btn = document.querySelector('.btn-toggle');
        if (!btn) return;
        var h = document.createElement('span');
        h.textContent = String.fromCodePoint(0x1F446);
        h.style.cssText = 'position:absolute;font-size:18px;pointer-events:none;z-index:99;margin-left:-6px;margin-top:-20px;animation:tapBounce .6s ease-in-out infinite,hintFade 3s ease forwards;';
        btn.style.position = 'relative';
        btn.parentNode.insertBefore(h, btn);
        function rm() { if (h.parentNode) h.parentNode.removeChild(h); document.removeEventListener('click', rm); }
        setTimeout(rm, 3200);
        document.addEventListener('click', rm);
      }, 600);
    });"""

html = html.replace("    window.addEventListener('DOMContentLoaded', recalc);", tap_js)

with open(path, 'w', encoding='utf-8') as f:
    f.write(html)

# Verify
with open(path, 'r', encoding='utf-8') as f:
    h = f.read()
print('ng items count:', len(re.findall(r'data-section="ng"', h)))
print('t2-total in recalc:', "setText('t2-total'" in h)
print('tap hint:', 'fromCodePoint' in h)
