import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
from PIL import Image, ImageTk
import io  # Import necessário para lidar com dados binários

# Dicionário de URLs das imagens de cada vegetal
vegetable_images = {
    "Batata": "https://i.pinimg.com/736x/ac/2d/b5/ac2db545397a4f1baaea5e7a572ec1fa.jpg",
    "Cenoura": "https://i.pinimg.com/736x/22/0e/f2/220ef2c061366eeef6019bec11e74755.jpg",
    "Quiabo": "https://i.pinimg.com/736x/d6/72/58/d6725890f3b306a0ada9b6cdce57a35a.jpg",
    "Ervilha": "https://i.pinimg.com/736x/9c/b7/be/9cb7beb2ed288f016d6a7c1e435f5802.jpg",
    "Milho": "https://i.pinimg.com/736x/0f/f1/78/0ff178e6c39a94791ac724a21ddb325a.jpg",
    "Inhame": "https://i.pinimg.com/736x/e6/21/46/e62146561a0c8f086449e23a3425dfa5.jpg",
    "Aipim": "https://i.pinimg.com/736x/8e/b6/5a/8eb65a66fce58d751c6a1efeb1a432b3.jpg",
    "Cebola": "https://i.pinimg.com/736x/08/69/b7/0869b7b0d6c7526e32f4a36e6b0ddc42.jpg",
    "Beterraba": "https://img.freepik.com/vetores-gratis/conjunto-de-desenhos-animados-de-beterraba_1308-131802.jpg",
    "Berinjela": "https://i.pinimg.com/736x/db/2f/d8/db2fd842a096d30f38d14f0f2170d71d.jpg",
    "Alho": "https://i.pinimg.com/736x/d1/69/1e/d1691e062dc617a74c3af7171f6ce9b2.jpg",
    "Abóbora": "https://i.pinimg.com/736x/f7/8d/31/f78d319e9cc6adfc5aba9f87378759ee.jpg",
    "Alface": "https://i.pinimg.com/736x/71/e0/7c/71e07cab5504450ea92047e2dc2d949c.jpg",
    "Alho-Poró": "https://i.pinimg.com/736x/b4/b8/d5/b4b8d5410338b64b22cbb7f0e7c26550.jpg",
    "Brócolis": "https://i.pinimg.com/736x/04/f8/88/04f88868489bc9a1902989dc6caa4ed0.jpg",
    "Espinafre": "https://i.pinimg.com/736x/b6/f6/20/b6f6200e6e7bffed9e6a1688dd717b6c.jpg",
    "Alcachofra": "https://i.pinimg.com/736x/62/a8/75/62a875698e37053965c6fac344e0ba50.jpg",
    "Agrião": "https://i.pinimg.com/736x/a5/db/6c/a5db6cafcf96ff2912eda14d54782bb0.jpg",
    "Rúcula": "https://media.istockphoto.com/id/954830520/vector/rucola-or-arugula-icon.jpg?s=612x612&w=0&k=20&c=QZ_9Iok9TZlyBndTI-M8vVgLFy7vFXIBnaZMYgFk7Tw=",
    "Repolho": "https://i.pinimg.com/736x/e5/f8/d6/e5f8d6a876f189371b081d5807955fc2.jpg",
    "Couve": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRDyIzhLOaWRqZ0QLS3sb6ZE9F8_whnDVLSGPw_7jRky_yap_uzJ78bonmpu4jzdbHSkW0&usqp=CAU",
    "Couve-Flor": "https://i.pinimg.com/736x/cb/90/0c/cb900c6423fa9378ed9c289228517d11.jpg"
}

def display_image():
    """Função para exibir a imagem do vegetal selecionado."""
    selected_vegetable = vegetable_combo.get()
    if selected_vegetable in vegetable_images:
        url = vegetable_images[selected_vegetable]
        try:
            with urlopen(url) as u:
                raw_data = u.read()
            img = Image.open(io.BytesIO(raw_data))

            # Define um tamanho fixo para a imagem
            fixed_width = 300
            fixed_height = 300
            img = img.resize((fixed_width, fixed_height), Image.LANCZOS)

            tk_img = ImageTk.PhotoImage(img)

            # Atualiza o rótulo da imagem
            image_label.config(image=tk_img, text="")
            image_label.image = tk_img
            image_label.config(width=fixed_width, height=fixed_height)
        except Exception as e:
            image_label.config(text=f"Erro ao carregar a imagem: {e}", image='')
    else:
        image_label.config(text="Imagem não encontrada", image='')

# Cria a janela principal
root = tk.Tk()
root.title("Visualizador de Imagens de Vegetais")
root.geometry("600x450")
root.configure(bg="lightblue")

# Adiciona um título
title_label = tk.Label(root, text="Selecione um vegetal para visualizar a imagem", font=("Arial", 18, "bold"), bg="lightblue", fg="#3B0053")
title_label.pack(pady=10)

# Cria uma caixa de seleção
vegetable_combo = ttk.Combobox(root, values=list(vegetable_images.keys()), state="readonly", font=("Arial", 12))
vegetable_combo.set("Selecione um vegetal")
vegetable_combo.pack(pady=10)

# Cria um botão para exibir a imagem
show_button = tk.Button(root, text="Exibir Imagem", command=display_image, font=("Arial", 12), bg="lightgreen")
show_button.pack(pady=10)

# Cria um rótulo para exibir a imagem
image_label = tk.Label(root, text="Imagem aparecerá aqui", font=("Arial", 14), bg="white", width=40, height=15)
image_label.pack(pady=20)

# Inicia o loop principal
root.mainloop()
