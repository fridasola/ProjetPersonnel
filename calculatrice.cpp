 #include <iostream>
 using namespace std;
 double calculer(double a, double b, char operateur){
    if (operateur=='+') return a+b;
    else if (operateur=='-') return a-b;
    else if (operateur=='*') return a*b;
    else if (operateur=='/') {
        if (b!=0) return a/b;
        else {
            cout<< "Erreur : division par zéro !" << endl;
            return 0;
        }
    } else {
        cout << "Opérateur non valide !" << endl;
        return 0;
    }
 }
 int main() {
    double nombre1, nombre2;
    char operateur;
    cout << "Entrez le premier nombre :";
    cin >> nombre1;

    cout<<"Entrez l'opérateur (+,-,*,/) :";
    cin>>operateur;

    cout<<"Entrez le deuxième nombre :";
    cin>>nombre2;
    double resultat = calculer(nombre1,nombre2,operateur);
    cout<<"Résultat :"<<resultat<<endl;
    return 0;
 }