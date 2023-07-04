from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Contact
from .serializers import ContactSerializer

@api_view(['POST'])
def identify(request):
    # Extract email and phoneNumber from request
    email = request.data.get('email')
    phoneNumber = request.data.get('phoneNumber')

    # Get primary contact
    primary_contact = Contact.objects.filter(phoneNumber=phoneNumber).first() if phoneNumber else Contact.objects.filter(email=email).first()
    
    if primary_contact is None:
        # Create new primary contact if doesn't exist
        new_contact = Contact.objects.create(
            email=email,
            phoneNumber=phoneNumber,
            linkPrecedence="primary"
        )
        return Response(ContactSerializer(new_contact).data, status=200)

    # Collect all related contacts
    related_contacts = Contact.objects.filter(
        linkedId=primary_contact.id
    ).order_by('createdAt')

    # Check if new info provided
    if primary_contact.phoneNumber != phoneNumber or primary_contact.email != email:
        if not phoneNumber or not email:
            pass
        else:
        # Create secondary contact if new info provided
            secondary_contact = Contact.objects.create(
                email=email,
                phoneNumber=phoneNumber,
                linkPrecedence="secondary",
                linkedId=primary_contact.id
            )
            related_contacts = list(related_contacts) + [secondary_contact]

    emails = set([c.email for c in [primary_contact] + list(related_contacts) if c.email])
    phoneNumbers = set([c.phoneNumber for c in [primary_contact] + list(related_contacts) if c.phoneNumber])
    secondaryContactIds = [c.id for c in related_contacts]

    return Response({
        "contact": {
            "primaryContactId": primary_contact.id,
            "emails": emails,
            "phoneNumbers": phoneNumbers,
            "secondaryContactIds": secondaryContactIds
        }
    }, status=200)
