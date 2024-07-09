from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, messagebox, filedialog, ttk, Scrollbar

import numpy as np
from sklearn import metrics
from matplotlib import pyplot, figure
from matplotlib.backends.backend_tkagg import FigureCanvasTk
import seaborn as sns

from Classifier import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"/Users/antoniusbagus/Library/CloudStorage/OneDrive-UniversitasSanataDharma/Skripsi/Klasifikasi-Varietas-Biji-Kopi-Arabika/assets/frame0")

clasifier = Classifier()


class main:
    def __init__(self):
        self.window = Tk()

        self.window.geometry("1284x685")
        self.window.configure(bg="#EAD8C0")
        self.window.title("Pendeteksi Varietas Kopi Arabika")

        self.canvas = Canvas(
            self.window,
            bg="#EAD8C0",
            height=685,
            width=1284,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)

        ################   Field Predict  #################
        self.entry_image_field_hasil_prediksi = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        entry_bg_1 = self.canvas.create_image(
            1177.4321060180664,
            579.0,
            image=self.entry_image_field_hasil_prediksi
        )

        self.field_hasil_prediksi = Entry(
            justify="center",
            bd=0,
            bg="#A79277",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.field_hasil_prediksi.place(
            x=1106.0,
            y=555.0,
            width=142.8642120361328,
            height=46.0
        )

        self.entry_image_sweetness = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            1008.0,
            636.0,
            image=self.entry_image_sweetness
        )
        self.entry_sweetness = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_sweetness.place(
            x=986.0,
            y=626.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            865.0,
            628.0,
            anchor="nw",
            text="Sweetness",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            865.0,
            628.0,
            anchor="nw",
            text="Sweetness",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_clean_cup = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        entry_bg_2 = self.canvas.create_image(
            1008.0,
            609.0,
            image=self.entry_image_entry_clean_cup
        )
        self.entry_clean_cup = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_clean_cup.place(
            x=986.0,
            y=599.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            865.0,
            601.0,
            anchor="nw",
            text="Clean.Cup",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_uniformity = PhotoImage(
            file=self.relative_to_assets("entry_3.png"))
        entry_bg_3 = self.canvas.create_image(
            1008.0,
            576.0,
            image=self.entry_image_entry_uniformity
        )
        self.entry_uniformity = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_uniformity.place(
            x=986.0,
            y=566.0,
            width=44.0,
            height=18.0
        )
        self.canvas.create_text(
            865.0,
            568.0,
            anchor="nw",
            text="Uniformity",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_acidity = PhotoImage(
            file=self.relative_to_assets("entry_4.png"))
        entry_bg_4 = self.canvas.create_image(
            1008.0,
            548.0,
            image=self.entry_image_entry_acidity
        )
        self.entry_acidity = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_acidity.place(
            x=986.0,
            y=538.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            865.0,
            540.0,
            anchor="nw",
            text="Acidity",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_body = PhotoImage(
            file=self.relative_to_assets("entry_5.png"))
        entry_bg_5 = self.canvas.create_image(
            1008.0,
            521.0,
            image=self.entry_image_entry_body
        )
        self.entry_body = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_body.place(
            x=986.0,
            y=511.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            865.0,
            513.0,
            anchor="nw",
            text="Body",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_aroma = PhotoImage(
            file=self.relative_to_assets("entry_6.png"))
        entry_bg_6 = self.canvas.create_image(
            812.0,
            636.0,
            image=self.entry_image_entry_aroma
        )
        self.entry_aroma = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_aroma.place(
            x=790.0,
            y=626.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            628.0,
            anchor="nw",
            text="Aroma",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_flavor = PhotoImage(
            file=self.relative_to_assets("entry_7.png"))
        entry_bg_7 = self.canvas.create_image(
            812.0,
            609.0,
            image=self.entry_image_entry_flavor
        )
        self.entry_flavor = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_flavor.place(
            x=790.0,
            y=599.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            601.0,
            anchor="nw",
            text="Flavor",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_aftertaste = PhotoImage(
            file=self.relative_to_assets("entry_8.png"))
        entry_bg_8 = self.canvas.create_image(
            812.0,
            576.0,
            image=self.entry_image_entry_aftertaste
        )
        self.entry_aftertaste = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_aftertaste.place(
            x=790.0,
            y=566.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            568.0,
            anchor="nw",
            text="AfterTaste",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_cupperpoint = PhotoImage(
            file=self.relative_to_assets("entry_9.png"))
        entry_bg_9 = self.canvas.create_image(
            812.0,
            548.0,
            image=self.entry_image_entry_cupperpoint
        )
        self.entry_cupperpoint = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_cupperpoint.place(
            x=790.0,
            y=538.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            540.0,
            anchor="nw",
            text="Cupper.Points",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_balance = PhotoImage(
            file=self.relative_to_assets("entry_10.png"))
        entry_bg_10 = self.canvas.create_image(
            812.0,
            521.0,
            image=self.entry_image_entry_balance
        )
        self.entry_balance = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_balance.place(
            x=790.0,
            y=511.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            513.0,
            anchor="nw",
            text="Balance",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        ################   Button Predict  #################
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.event_button_predict(self.entry_balance,
                                                      self.entry_cupperpoint,
                                                      self.entry_aftertaste,
                                                      self.entry_flavor,
                                                      self.entry_aroma,
                                                      self.entry_body,
                                                      self.entry_acidity,
                                                      self.entry_uniformity,
                                                      self.entry_clean_cup,
                                                      self.entry_sweetness),
            relief="flat"
        )
        self.button_1.place(
            x=1174.0,
            y=513.0,
            width=80.0,
            height=20.0
        )

        ####################   CM    ######################
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        image_1 = self.canvas.create_image(
            965.0,
            362.0,
            image=self.image_image_1
        )


        self.canvas.create_text(
            897.0,
            224.0,
            anchor="nw",
            text="Confusion Matrix",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        ################   Button Hitung Klasifikasi  #################
        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.event_button_clasify(knn = self.entry_jumlah_knn,
                                                      cv = self.entry_jumlah_cv,
                                                      attribut = self.entry_jumlah_attribut),
            relief="flat"
        )
        self.button_2.place(
            x=1174.0,
            y=127.0,
            width=80.0,
            height=20.0
        )

        self.image_field_hasil_akurasi = PhotoImage(
            file=self.relative_to_assets("entry_11.png"))
        entry_bg_11 = self.canvas.create_image(
            1181.4321060180664,
            181.0,
            image=self.image_field_hasil_akurasi
        )

        self.field_hasil_akurasi = Entry(
            justify="center",
            bd=0,
            bg="#A79277",
            fg="#FFFFFF",
            highlightthickness=0
        )
        self.field_hasil_akurasi.place(
            x=1110.0,
            y=157.0,
            width=142.8642120361328,
            height=46.0
        )

        self.entry_image_entry_jumlah_attribut = PhotoImage(
            file=self.relative_to_assets("entry_12.png"))
        entry_bg_12 = self.canvas.create_image(
            812.0,
            195.0,
            image=self.entry_image_entry_jumlah_attribut
        )
        self.entry_jumlah_attribut = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_jumlah_attribut.place(
            x=790.0,
            y=185.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            187.0,
            anchor="nw",
            text="Attribute",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_jumlah_cv = PhotoImage(
            file=self.relative_to_assets("entry_13.png"))
        entry_bg_13 = self.canvas.create_image(
            812.0,
            167.0,
            image=self.entry_image_entry_jumlah_cv
        )
        self.entry_jumlah_cv = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_jumlah_cv.place(
            x=790.0,
            y=157.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            159.0,
            anchor="nw",
            text="Cross Validation",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        self.entry_image_entry_jumlah_knn = PhotoImage(
            file=self.relative_to_assets("entry_14.png"))
        entry_bg_14 = self.canvas.create_image(
            812.0,
            140.0,
            image=self.entry_image_entry_jumlah_knn
        )
        self.entry_jumlah_knn = Entry(
            justify="center",
            bd=0,
            bg="#D1BB9E",
            fg="#000716",
            highlightthickness=0
        )
        self.entry_jumlah_knn.place(
            x=790.0,
            y=130.0,
            width=44.0,
            height=18.0
        )

        self.canvas.create_text(
            669.0,
            132.0,
            anchor="nw",
            text="KNN",
            fill="#000000",
            font=("Inter Bold", 12 * -1)
        )

        ###############   Data Terproses  ################
        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        image_2 = self.canvas.create_image(
            319.0,
            535.0,
            image=self.image_image_2
        )

        ################   Button preprosees  #################
        self.button_image_button_preproses = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_preproses = Button(
            image=self.button_image_button_preproses,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.event_button_preproses(),
            relief="flat"
        )
        self.button_preproses.place(
            x=27.0,
            y=385.0,
            width=108.0,
            height=20.0
        )
        ######################################################

        ################   Button Import  #################
        self.button_image_button_show_data = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_show_data = Button(
            image=self.button_image_button_show_data,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.event_button_show_data(),
            relief="flat"
        )
        self.button_show_data.place(
            x=27.0,
            y=100.0,
            width=80.0,
            height=20.0
        )

        ##############   Data Mentah   ###################
        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        image_3 = self.canvas.create_image(
            319.0,
            247.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        image_4 = self.canvas.create_image(
            640.0,
            40.0,
            image=self.image_image_4
        )

        self.canvas.create_text(
            644.0,
            18.0,
            anchor="nw",
            text="Pendeteksi Varietas Kopi Arabika",
            fill="#FFF2E1",
            font=("Inter ExtraBold", 36 * -1)
        )

        self.image_image_5 = PhotoImage(
            file=self.relative_to_assets("image_5.png"))
        image_5 = self.canvas.create_image(
            47.0,
            39.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=self.relative_to_assets("image_6.png"))
        image_6 = self.canvas.create_image(
            1246.0,
            25.0,
            image=self.image_image_6
        )

        self.window.resizable(False, False)
        self.window.mainloop()


        temp = clasifier.GetDataSet()
        temp = clasifier.PrepData(temp)
        cm = clasifier.CalculateAcuracy(temp, 3, 3, 3)


    def relative_to_assets(self, path: str) -> Path:
        return ASSETS_PATH / Path(path)


    def event_button_predict(self, balance, cupper_points, aftertaste, flavor, aroma, body, acidity, uniformity,
                             clean_cup,
                             sweetness):
        try:
            balance_value = float(balance.get())
            cupper_point_value = float(cupper_points.get())
            aftertaste_value = float(aftertaste.get())
            flavor_value = float(flavor.get())
            aroma_value = float(aroma.get())
            body_value = float(body.get())
            acidity_value = float(acidity.get())
            uniformity_value = float(uniformity.get())
            clean_cup_value = float(clean_cup.get())
            sweetness_value = float(sweetness.get())

            if balance_value < 0 or balance_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif cupper_point_value < 0 or cupper_point_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif aftertaste_value < 0 or aftertaste_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif flavor_value < 0 or flavor_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif aroma_value < 0 or aroma_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif body_value < 0 or body_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif acidity_value < 0 or acidity_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif uniformity_value < 0 or uniformity_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif clean_cup_value < 0 or clean_cup_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            elif sweetness_value < 0 or sweetness_value > 10:
                messagebox.showerror("showerror", "Angka Harus Bernilai 0 - 10")
            else:
                testing = {'Aroma': [aroma_value],
                           'Flavor': [flavor_value],
                           'Aftertaste': [aftertaste_value],
                           'Acidity': [acidity_value],
                           'Body': [body_value],
                           'Uniformity': [uniformity_value],
                           'Balance': [balance_value],
                           'Clean.Cup': [clean_cup_value],
                           'Sweetness': [sweetness_value],
                           'Cupper.Points': [cupper_point_value]}
                testing_df = pd.DataFrame(testing)
                testing_df = clasifier.NormalizeTestingData(testing_df)
                pred_result = clasifier.Predict(testing_df)
                if pred_result == 1:
                    pred_result = 'Diprediksi Bourbon'
                elif pred_result == 2:
                    pred_result = 'Diprediksi Caturra'
                elif pred_result == 3:
                    pred_result = 'Diprediksi Typica'
                self.field_hasil_prediksi.delete(0, 'end')
                self.field_hasil_prediksi.insert(0, pred_result)

        except ValueError:
            messagebox.showerror("showerror",
                                 "Input Salah Atau Belum Di Isi Semua !!!\n "
                                 "Harus Berisi Angka dan Harus Bernilai 0 - 10\n"
                                 "Jika Angka Bernilai Koma Gunakan (.) cth 9.5")

    def event_button_show_data(self):
        global output_path
        output_path = filedialog.askopenfile()

        #data = clasifier.GetDataSet()
        self.data = pd.read_csv(output_path)

        table_columns = list(self.data.columns.values)
        table_data = self.data.to_numpy().tolist()

        tree_vertical_scroll = ttk.Scrollbar(self.canvas, orient="vertical")
        tree_vertical_scroll.place(x=583, y=152, height=193, width=15)
        tree_horizontal_scroll = ttk.Scrollbar(self.canvas, orient="horizontal")
        tree_horizontal_scroll.place(x=40, y=330, height=15, width=543)

        table = ttk.Treeview(self.canvas, columns=table_columns, show='headings', yscrollcommand = tree_vertical_scroll,
                             xscrollcommand=tree_horizontal_scroll)
        table.place(x=40, y=152, height=178, width=543)

        for i in table_columns:
            table.column(i)
            table.heading(i, text=i)
        for dt in table_data:
            v = [r for r in dt]
            table.insert('', 'end', iid=v[0], values=v)

        tree_vertical_scroll.config(command=table.yview)
        tree_horizontal_scroll.config(command=table.xview)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Treeview", background='#D1BB9E', foreground='black')
        style.configure("Treeview.Heading", background='#A79277', foreground='black')
        style.map("Treeview", background=[("selected","#A79277")])

        style.configure('Horizontal.TScrollbar', background="#D1BB9E")
        style.configure('Vertical.TScrollbar', background="#D1BB9E")

    def event_button_preproses(self):
        try:
            self.data = clasifier.PrepData(self.data)
            table_columns = list(self.data.columns.values)
            table_data = self.data.to_numpy().tolist()

            tree_vertical_scroll = ttk.Scrollbar(self.canvas, orient="vertical")
            tree_vertical_scroll.place(x=583, y=439, height=193, width=15)
            tree_horizontal_scroll = ttk.Scrollbar(self.canvas, orient="horizontal")
            tree_horizontal_scroll.place(x=40, y=617, height=15, width=543)

            table = ttk.Treeview(self.canvas, columns=table_columns, show='headings',
                                 yscrollcommand=tree_vertical_scroll,
                                 xscrollcommand=tree_horizontal_scroll)
            table.place(x=40, y=439, height=178, width=543)

            for i in table_columns:
                table.column(i)
                table.heading(i, text=i)
            for dt in table_data:
                v = [r for r in dt]
                table.insert('', 'end', values=v)

            tree_vertical_scroll.config(command=table.yview)
            tree_horizontal_scroll.config(command=table.xview)

            style = ttk.Style()
            style.theme_use('default')
            style.configure("Treeview", background='#D1BB9E', foreground='black')
            style.configure("Treeview.Heading", background='#A79277', foreground='black')
            style.map("Treeview", background=[("selected", "#A79277")])

            style.configure('Horizontal.TScrollbar', background="#D1BB9E")
            style.configure('Vertical.TScrollbar', background="#D1BB9E")
        except AttributeError:
            messagebox.showerror("showerror",
                                 "Harap Import Dataset Terlebih Dahulu")

    def event_button_clasify(self, knn, cv, attribut):
        try:
            temp = clasifier.CalculateAcuracy(self.data, int(knn.get()), int(cv.get()), int(attribut.get()))
            akurasi = round(temp[0], 2)
            akurasi = akurasi*100
            text = "Akurasi : " + str(akurasi) + " %"
            self.field_hasil_akurasi.delete(0, 'end')
            self.field_hasil_akurasi.insert(0, text)

            d = temp[1]

            entry_image_16 = PhotoImage(
                file=self.relative_to_assets("entry_16.png"))
            entry_bg_16 = self.canvas.create_image(
                905.5,
                301.5,
                image=entry_image_16
            )
            entry_16 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_16.place(
                x=874.0,
                y=270.0,
                width=59.0,
                height=59.0
            )

            entry_image_17 = PhotoImage(
                file=self.relative_to_assets("entry_17.png"))
            entry_bg_17 = self.canvas.create_image(
                967.0,
                301.5,
                image=entry_image_17
            )
            entry_17 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_17.place(
                x=937.0,
                y=270.0,
                width=59.0,
                height=59.0
            )

            entry_image_18 = PhotoImage(
                file=self.relative_to_assets("entry_18.png"))
            entry_bg_18 = self.canvas.create_image(
                1027.0,
                301.5,
                image=entry_image_18
            )
            entry_18 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_18.place(
                x=997.0,
                y=270.0,
                width=59.0,
                height=59.0
            )

            entry_image_19 = PhotoImage(
                file=self.relative_to_assets("entry_19.png"))
            entry_bg_19 = self.canvas.create_image(
                905.5,
                363.0,
                image=entry_image_19
            )
            entry_19 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_19.place(
                x=874.0,
                y=333.0,
                width=59.0,
                height=59.0
            )

            entry_image_20 = PhotoImage(
                file=self.relative_to_assets("entry_20.png"))
            entry_bg_20 = self.canvas.create_image(
                967.0,
                363.0,
                image=entry_image_20
            )
            entry_20 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_20.place(
                x=937.0,
                y=333.0,
                width=59.0,
                height=59.0
            )

            entry_image_21 = PhotoImage(
                file=self.relative_to_assets("entry_21.png"))
            entry_bg_21 = self.canvas.create_image(
                1027.0,
                363.0,
                image=entry_image_21
            )
            entry_21 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_21.place(
                x=997.0,
                y=333.0,
                width=59.0,
                height=59.0
            )

            entry_image_22 = PhotoImage(
                file=self.relative_to_assets("entry_22.png"))
            entry_bg_22 = self.canvas.create_image(
                905.5,
                423.0,
                image=entry_image_22
            )
            entry_22 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_22.place(
                x=874.0,
                y=393.0,
                width=59.0,
                height=59.0
            )

            entry_image_23 = PhotoImage(
                file=self.relative_to_assets("entry_23.png"))
            entry_bg_23 = self.canvas.create_image(
                967.0,
                423.0,
                image=entry_image_23
            )
            entry_23 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_23.place(
                x=937.0,
                y=393.0,
                width=59.0,
                height=59.0
            )

            entry_image_24 = PhotoImage(
                file=self.relative_to_assets("entry_24.png"))
            entry_bg_24 = self.canvas.create_image(
                1027.0,
                423.0,
                image=entry_image_24
            )
            entry_24 = Entry(
                bd=0,
                bg="#FFF2E1",
                fg="#000716",
                highlightthickness=0,
                justify="center"
            )
            entry_24.place(
                x=997.0,
                y=393.0,
                width=59.0,
                height=59.0
            )
#
            self.canvas.create_rectangle(
                873.0,
                332.0,
                1057.0,
                333.0,
                fill="#A79277",
                outline="")

            self.canvas.create_rectangle(
                873.0,
                392.0,
                1057.0,
                393.0,
                fill="#A79277",
                outline="")
#
            self.canvas.create_rectangle(
                936.0,
                270.0,
                937.0,
                454.0,
                fill="#A79277",
                outline="")

            self.canvas.create_rectangle(
                996.0,
                270.0,
                997.0,
                454.0,
                fill="#A79277",
                outline="")

            self.canvas.create_text(
                886.0,
                255.0,
                anchor="nw",
                text="Bourbon",
                fill="#A79277",
                font=("Inter Bold", 10 * -1)
            )

            self.canvas.create_text(
                947.0,
                256.0,
                anchor="nw",
                text="Caturra",
                fill="#A79277",
                font=("Inter Bold", 10 * -1)
            )

            self.canvas.create_text(
                1010.0,
                256.0,
                anchor="nw",
                text="Typica",
                fill="#A79277",
                font=("Inter Bold", 10 * -1)
            )

            self.canvas.create_text(
                823.0,
                295.0,
                anchor="nw",
                text="Bourbon",
                fill="#A79277",
                font=("Inter Bold", 10 * -1)
            )

            self.canvas.create_text(
                823.0,
                357.0,
                anchor="nw",
                text="Caturra",
                fill="#A79277",
                font=("Inter Bold", 10 * -1)
            )

            self.canvas.create_text(
                823.0,
                419.0,
                anchor="nw",
                text="Typica",
                fill="#A79277",
                font=("Inter Bold", 10 * -1)
            )

            entry_16.delete(0, 'end')
            entry_17.delete(0, 'end')
            entry_18.delete(0, 'end')
            entry_19.delete(0, 'end')
            entry_20.delete(0, 'end')
            entry_21.delete(0, 'end')
            entry_22.delete(0, 'end')
            entry_23.delete(0, 'end')
            entry_24.delete(0, 'end')

            entry_16.insert(0, d[0][0])
            entry_17.insert(0, d[0][1])
            entry_18.insert(0, d[0][2])
            entry_19.insert(0, d[1][0])
            entry_20.insert(0, d[1][1])
            entry_21.insert(0, d[1][2])
            entry_22.insert(0, d[2][0])
            entry_23.insert(0, d[2][1])
            entry_24.insert(0, d[2][2])





        except AttributeError:
            messagebox.showerror("showerror",
                                 "Harap Import Dataset Terlebih Dahulu Dan Lakukan Pre-Processed Data")
        except ValueError:
            messagebox.showerror("showerror",
                                 "Input Harus Di Isi Dahulu !!!\n "
                                 "Harus Berisi Angka !!!\n")




if __name__ == "__main__":
    main()
