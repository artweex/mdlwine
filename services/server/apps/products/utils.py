from django.utils.text import slugify
import uuid

def create_slug(sender, instance, new_slug = None):
    slug = new_slug if new_slug else slugify(instance.title)
    qs = sender.objects.filter(slug = slug).order_by("-id")
    if not qs.exists():
        return slug
    qsitem = qs.first()
    qid = qsitem.id if qsitem else uuid.uuid4().hex[:6]
    _new_slug = f"{slug}-{qid}"
    return create_slug(sender = sender, instance = instance, new_slug = _new_slug)
    
