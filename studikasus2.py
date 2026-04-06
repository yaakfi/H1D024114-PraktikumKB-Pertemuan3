import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# VARIABEL INPUT (Antecedent)
kejelasan_informasi = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_informasi')
kejelasan_persyaratan = ctrl.Antecedent(np.arange(0, 101), 'kejelasan_persyaratan')
kemampuan_petugas = ctrl.Antecedent(np.arange(0, 101), 'kemampuan_petugas')
ketersediaan_sarpras = ctrl.Antecedent(np.arange(0, 101), 'ketersediaan_sarpras')
# VARIABEL MENAMPILKAN HASIL AKHIR (Consequent)
kepuasan_pelayanan = ctrl.Consequent(np.arange(0, 401), 'kepuasan_pelayanan')

# PEMBENTUKAN HIMPUNAN FUZZY INPUT
# KEJELASAN INFORMASI
kejelasan_informasi['tidak memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [0, 60, 75])
kejelasan_informasi['cukup memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [60, 75, 90])
kejelasan_informasi['memuaskan'] = fuzz.trimf(kejelasan_informasi.universe, [75, 90, 100])

# KEJELASAN PERSYARATAN
kejelasan_persyaratan['tidak memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [0, 60, 75])
kejelasan_persyaratan['cukup memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [60, 75, 90])
kejelasan_persyaratan['memuaskan'] = fuzz.trimf(kejelasan_persyaratan.universe, [75, 90, 100])

# KEMAMPUAN PETUGAS
kemampuan_petugas['tidak memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [0, 60, 75])
kemampuan_petugas['cukup memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [60, 75, 90])
kemampuan_petugas['memuaskan'] = fuzz.trimf(kemampuan_petugas.universe, [75, 90, 100])

# KETERSEDIAAN SARPRAS
ketersediaan_sarpras['tidak memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [0, 60, 75])
ketersediaan_sarpras['cukup memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [60, 75, 90])
ketersediaan_sarpras['memuaskan'] = fuzz.trimf(ketersediaan_sarpras.universe, [75, 90, 100])

# PEMBENTUKAN HIMPUNAN FUZZY MENAMPILKAN HASIL AKHIR
kepuasan_pelayanan['tidak memuaskan'] = fuzz.trimf(kepuasan_pelayanan.universe, [0, 50, 75])
kepuasan_pelayanan['kurang memuaskan'] = fuzz.trimf(kepuasan_pelayanan.universe, [50, 75, 100])
kepuasan_pelayanan['cukup memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [100, 150, 250, 275])
kepuasan_pelayanan['memuaskan'] = fuzz.trapmf(kepuasan_pelayanan.universe, [250, 275, 325, 350])
kepuasan_pelayanan['sangat memuaskan'] = fuzz.trimf(kepuasan_pelayanan.universe, [325, 350, 400])

# DAFTAR ATURAN FUZZY (RULES)
aturan_1 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['kurang memuaskan'])
aturan_2 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_3 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_4 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_5 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_6 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_7 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_8 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_9 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_10 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_11 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_12 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_13 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_14 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_15 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_16 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_17 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_18 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_19 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_20 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_21 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_22 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_23 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_24 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_25 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_26 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_27 = ctrl.Rule(kejelasan_informasi['tidak memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_28 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_29 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_30 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_31 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_32 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_33 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_34 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_35 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_36 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_37 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_38 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_39 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_40 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_41 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_42 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_43 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_44 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_45 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_46 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_47 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_48 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_49 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_50 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_51 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_52 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_53 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_54 = ctrl.Rule(kejelasan_informasi['cukup memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_55 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_56 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_57 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_58 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_59 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_60 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_61 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_62 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_63 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['tidak memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_64 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['cukup memuaskan'])
aturan_65 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_66 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_67 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_68 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_69 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_70 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_71 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_72 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['cukup memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_73 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_74 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_75 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['tidak memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_76 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['memuaskan'])
aturan_77 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_78 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['cukup memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_79 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['tidak memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_80 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['cukup memuaskan'], kepuasan_pelayanan['sangat memuaskan'])
aturan_81 = ctrl.Rule(kejelasan_informasi['memuaskan'] & kejelasan_persyaratan['memuaskan'] & kemampuan_petugas['memuaskan'] & ketersediaan_sarpras['memuaskan'], kepuasan_pelayanan['sangat memuaskan'])

# PEMBUATAN SISTEM INFERENSI
pengatur_fuzzy = ctrl.ControlSystem([aturan_1, aturan_2, aturan_3, aturan_4, aturan_5, aturan_6, aturan_7, aturan_8, aturan_9, aturan_10, aturan_11, aturan_12, aturan_13, aturan_14, aturan_15, aturan_16,
aturan_17, aturan_18, aturan_19, aturan_20, aturan_21, aturan_22, aturan_23, aturan_24, aturan_25, aturan_26, aturan_27, aturan_28, aturan_29, aturan_30, aturan_31, 
aturan_32, aturan_33, aturan_34, aturan_35, aturan_36, aturan_37, aturan_38, aturan_39, aturan_40, aturan_41, aturan_42, aturan_43, aturan_44, aturan_45, aturan_46, aturan_47, aturan_48, aturan_49, aturan_50, 
aturan_51, aturan_52, aturan_53, aturan_54, aturan_55, aturan_56, aturan_57, aturan_58, aturan_59, aturan_60, aturan_61, aturan_62, aturan_63, aturan_64, aturan_65, aturan_66, aturan_67, aturan_68, aturan_69, 
aturan_70, aturan_71, aturan_72, aturan_73, aturan_74, aturan_75, aturan_76, aturan_77, aturan_78, aturan_79, aturan_80, aturan_81])

simulasi_fuzzy = ctrl.ControlSystemSimulation(pengatur_fuzzy)

# MEMASUKKAN NILAI INPUT
simulasi_fuzzy.input['kejelasan_informasi'] = 80
simulasi_fuzzy.input['kejelasan_persyaratan'] = 60
simulasi_fuzzy.input['kemampuan_petugas'] = 50
simulasi_fuzzy.input['ketersediaan_sarpras'] = 90

# PROSES DEFUZZIFIKASI
simulasi_fuzzy.compute()

# MENAMPILKAN HASIL AKHIR
print(f"Skor Akhir Kepuasan: {simulasi_fuzzy.output['kepuasan_pelayanan']:.2f}")

# Plotting Grafik
kejelasan_informasi.view()
kejelasan_persyaratan.view()
kemampuan_petugas.view()
ketersediaan_sarpras.view()
kepuasan_pelayanan.view()

kepuasan_pelayanan.view(sim=simulasi_fuzzy)

# Agar grafik tidak memblokir terminal
plt.show(block=False)

# Jeda agar layar terminal tidak langsung close
input("\nTekan ENTER untuk menutup aplikasi & grafik...")
plt.close('all')
