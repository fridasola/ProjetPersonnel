let essaie=1;
function oui(){
    const reponsepositive = document.querySelector("div");
    reponsepositive.innerHTML="Super";
    let affichageessaie='Au bout de'
    if (essaie > 1){
        affichageessaie=affichageessaie+essaie+'essaie';
        console.log(affichageessaie);
    }
}