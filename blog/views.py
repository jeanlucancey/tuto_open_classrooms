from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Article

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

# def view_article(request, id_article):
#     """ 
#     Vue qui affiche un article selon son identifiant (ou ID, ici un numéro)
#     Son ID est le second paramètre de la fonction (pour rappel, le premier
#     paramètre est TOUJOURS la requête de l'utilisateur)
#     """
#     return HttpResponse(
#         "Vous avez demandé l'article n° {0} !".format(id_article)    
#     )

def view_article(request, id_article):
    # Si l'ID est supérieur à 100, nous considérons que l'article n'existe pas
    if int(id_article) > 100:
        raise Http404

    return HttpResponse('<h1>Mon article [%d] ici</h1>' % (int(id_article)))
#    return redirect(view_redirection)
#    return redirect(view_article, id_article=42)
#    return redirect('afficher_article', id_article=42)

def view_redirection(request):
    return HttpResponse("Vous avez été redirigé.")

def list_articles(request, month, year):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)  
    )

# def list_articles(request, year, month=1):
#     return HttpResponse('Articles de %s/%s' % (year, month))

def list_articles_by_tag(request, tag):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé le tag {}.".format(tag)  
    )

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

def ma_page(request):
    max_multiplicande = 5
    max_multiplicateur = 3
    mes_lignes = []
    for multiplicande in range(max_multiplicande):
        for multiplicateur in range(max_multiplicateur):
            resultat = multiplicande * multiplicateur
            maLigne = "%d x %d = %d" % (multiplicande, multiplicateur, resultat)
            mes_lignes.append(maLigne)
        if multiplicande != max_multiplicande - 1:
            mes_lignes.append('---')
    return render(request, 'blog/mapage.html', locals())

def afficher_article(request, nombre1):
    nombre2 = nombre1
    total = 2 * nombre1
    return render(request, 'blog/addition.html', locals())

def accueil(request):
    """ Afficher tous les articles de notre blog """
    articles = Article.objects.all() # Nous sélectionnons tous nos articles
    return render(request, 'blog/accueil.html', {'derniers_articles': articles})

def lire(request, id):
    """ Afficher un article complet """
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})
