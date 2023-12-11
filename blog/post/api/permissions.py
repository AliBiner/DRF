from rest_framework.permissions import BasePermission

class IsOwner(BasePermission):

    # def has_permission(self, request, view): bu method bir transist'dir ve ilk bu method çalışır.
    #     print("çalıştı has_perm")
    #     return True
    def has_permission(self, request, view, obj): #burada kullanma nedenimiz sayfa yüklenirkende yetkilendirmeleri kontrol etmek. aksi takdirde sayfa yüklendikten sonra kontrolleri gerçekleştirir.
        return request.user and request.user.is_authenticated
    message = 'You must be the owner of this object'
    def has_object_permission(self, request, view, obj): #bu method ise http'i type uyuştuğunda çalışır. eğer delete ise post gelince çalışmaz.

        return obj.user == request.user or request.user.is_superuser

