let essaie = 1;
let affichageessaie = '<3';  // Message initial

function positif() {
    let apparaitrereponse = document.querySelector("#reponse");
    if (essaie > 1) {
        affichageessaie = 'Au bout de ' + essaie + ' essais ;(';
    }
    apparaitrereponse.innerHTML = "Super ! " + affichageessaie;
    apparaitrereponse.classList.remove("hidden");
    lancerCoeurs();
}

function negatif() {
    essaie++;  // Incrémenter le nombre d'essais

    
    const boutonNon = document.getElementById("non");
    boutonNon.style.transform = `scale(${1 - essaie * 0.1})`;  // Ajouter la classe qui rétrécit le bouton
    const messageNon = document.getElementById("messageNon");
    messageNon.classList.remove("hidden");  // Afficher le message

    // Optionnel : cacher le message après 3 secondes
    setTimeout(function() {
        messageNon.classList.add("hidden");  // Cacher le message après 3 secondes
    }, 3000); // 3000ms = 3 secondes

    if (essaie > 5) {
        document.body.style.background = 'linear-gradient(135deg, rgb(142, 45, 45), #ff477e)';
    }
    
}

function lancerCoeurs() {
    const container = document.createElement("div");
    container.classList.add("hearts-container");
    document.body.appendChild(container);

    for (let i = 0; i < 15; i++) { // Générer 15 cœurs
        setTimeout(() => {
            const heart = document.createElement("div");
            heart.classList.add("heart");
            heart.innerHTML = "♡";
            

            // Position aléatoire sur l'écran
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.top = "100vh"; // Commence en bas
            heart.style.fontSize = Math.random() * 20 + 20 + "px"; // Tailles variées

            container.appendChild(heart);

            // Supprimer le cœur après l'animation
            setTimeout(() => {
                heart.remove();
            }, 3000);
        }, i * 200); // Espacement entre chaque cœur
    }
}
