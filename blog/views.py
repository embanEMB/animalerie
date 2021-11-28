from django.shortcuts import render, get_object_or_404, redirect
from .models import Animal, Equipement
from .forms import MoveForm

# Create your views here.

def animal_list(request):
    animals = Animal.objects.filter()
    equipements = Equipement.objects.filter()
    return render(request, 'blog/animal_list.html', {'animals': animals, 'equipements': equipements})

def equipement_list(request):
    equipements = Equipement.objects.filter()
    return render(request, 'blog/equipement_list.html', {'equipements': equipements})
 
def animal_detail(request, id_animal):
    animal = get_object_or_404(Animal, id_animal=id_animal)
    #lieu=animal.lieu
    form=MoveForm()
    if request.method == "POST":
        ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
        form = MoveForm(request.POST, instance=animal)
        if form.is_valid():
            nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
            message=''
            # if nouveau_lieu.id_equip=='Litière':
            #     nouveau_lieu.disponibilite='libre'
            #     nouveau_lieu.save()
            if nouveau_lieu.disponibilite=='libre':
                if nouveau_lieu.id_equip == 'Mangeoire': #nourrir
                    if animal.etat =='affamé':
                        animal.etat='repus'
                        animal.save()
                        ancien_lieu.disponibilite='libre'
                        ancien_lieu.save()
                        nouveau_lieu.disponibilite='occupé'
                        nouveau_lieu.save()
                        return redirect('animal_detail', id_animal=id_animal)
                    else :
                        message=str(animal.id_animal)+' n\'a pas faim.'                      
                        #return render(request, 'blog/animal_detail.html', {'animal': animal, 'lieu': ancien_lieu.id_equip, 'form': form, 'message': message})
                        return render({'animal': animal, 'lieu': ancien_lieu.id_equip, 'form': form, 'message': message}, 'blog/animal_detail.html')
                elif nouveau_lieu.id_equip=='Roue': #divertir
                    if animal.etat =='repus':
                        animal.etat='fatigué'
                        animal.save()
                        ancien_lieu.disponibilite='libre'
                        ancien_lieu.save()
                        nouveau_lieu.disponibilite='occupé'
                        nouveau_lieu.save()
                        return redirect('animal_detail', id_animal=id_animal)
                    else :
                        message=str(animal.id_animal)+' n\'est pas en état de faire du sport.'                      
                        return render(request, 'blog/animal_detail.html', {'animal': animal, 'lieu': ancien_lieu, 'form': form, 'message': message})
                elif nouveau_lieu.id_equip=='Nid': #coucher
                    if animal.etat == 'fatigué':
                        animal.etat='endormi'
                        animal.save()
                        ancien_lieu.disponibilite='libre'
                        ancien_lieu.save()
                        nouveau_lieu.disponibilite='occupé'
                        nouveau_lieu.save()
                        return redirect('animal_detail', id_animal=id_animal)
                    else :
                        message=str(animal.id_animal)+' n\'est pas fatigué.'                      
                        return render(request, 'blog/animal_detail.html', {'animal': animal, 'lieu': ancien_lieu, 'form': form, 'message': message})    
                elif nouveau_lieu.id_equip=='Litière': #réveiller
                    animal.etat='affamé'
                    animal.save()
                    ancien_lieu.disponibilite='libre'
                    ancien_lieu.save()
                    nouveau_lieu.disponibilite='occupé'
                    nouveau_lieu.save()
                    return redirect('animal_detail', id_animal=id_animal)
            if nouveau_lieu.disponibilite=='occupé':
                if nouveau_lieu.id_equip=='Litière':
                    message = ''
                else :
                    message='Le/la '+str(nouveau_lieu.id_equip)+' est occupé(e).'
                #form.save(commit=False)                
                return render(request, 'blog/animal_detail.html', {'animal': animal, 'lieu': ancien_lieu, 'form': form, 'message': message})
                #return render({'animal': animal, 'lieu': ancien_lieu.id_equip, 'form': form, 'message': message}, 'blog/animal_detail.html')
    else:
        message= ''
        form = MoveForm()
        return render(request,
                  'blog/animal_detail.html',
                  {'animal': animal, 'lieu': animal.lieu, 'form': form,'message':message})

# def equipement_list(request):
#     equipements = Equipement.objects.filter()
#     return render(request, 'blog/equipement_list.html', {'equipements': equipements})

# def equipement_detail(request, id_equip):
#     equipement = get_object_or_404(Equipement, id_equip=id_equip)
#     form=MoveForm()
#     if request.method == "POST":
#         form = MoveForm(request.POST, instance=equipement)
#     else:
#         form = MoveForm()
#     if form.is_valid():
#         ancien_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
#         ancien_lieu.disponibilite = "libre"
#         ancien_lieu.save()
#         form.save()
#         nouveau_lieu = get_object_or_404(Equipement, id_equip=animal.lieu.id_equip)
#         nouveau_lieu.disponibilite = "occupé"
#         nouveau_lieu.save()
#         return redirect('equip_detail', id_animal=id_animal)
#     else:
#         form = MoveForm()
#         form.save(commit=False) 
#         return render(request,
#                   'blog/animal_detail.html',
#                   {'animal': animal, 'lieu': animal.lieu, 'form': form})