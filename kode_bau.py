"""Modul contoh sederhana untuk demonstrasi kode yang mengikuti PEP 8."""


def calculate_result(a, b, c, values, extra, offset):
    """Hitung hasil penjumlahan berdasarkan kondisi tertentu.

    Args:
        a (bool): Flag kondisi pertama.
        b (bool): Flag kondisi kedua.
        c: Nilai kondisi ketiga, biasanya None atau nilai lain.
        values (list): List berisi nilai numerik.
        extra (int): Nilai tambahan untuk perhitungan.
        offset (int): Nilai offset tambahan.

    Returns:
        int or None: Hasil perhitungan, atau None jika kondisi tidak terpenuhi.
    """
    counter = 1
    base = 0

    if a and not b and c is None:
        result = values[0] + extra + counter + base
        return result

    return None


def main():
    """Titik masuk utama program."""
    output = calculate_result(True, False, None, [2], 1, 3)
    print(output)


if __name__ == "__main__":
    main()
