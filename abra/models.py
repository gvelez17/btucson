from django.db import models
from treebeard.mp_tree import MP_Node

class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def __unicode__(self):
        return 'Category: %s' % self.name
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class AbAccessPermissions(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    cid = models.BigIntegerField(blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    access_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_access_permissions'


class AbAdshare(models.Model):
    google_client_id = models.CharField(max_length=64, blank=True, null=True)
    is_donation = models.CharField(max_length=1, blank=True, null=True)
    code_snippet = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    user_id = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_adshare'


class AbAdshareOrgs(models.Model):
    id = models.IntegerField(blank=True, null=True)
    google_client_id = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=128, blank=True, null=True)
    registered_by = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_adshare_orgs'


class AbBizOrg(models.Model):
    id = models.BigIntegerField(unique=True, blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=25, blank=True, null=True)
    zip4 = models.CharField(max_length=10, blank=True, null=True)
    local_ownop = models.CharField(max_length=1, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    blong = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_biz_org'


class AbCatTypes(models.Model):
    cid = models.BigIntegerField(blank=True, null=True)
    tablename = models.CharField(max_length=32, blank=True, null=True)
    catcode = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_cat_types'


class AbEats(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    neighborhood = models.CharField(max_length=255, blank=True, null=True)
    cross_street = models.CharField(max_length=255, blank=True, null=True)
    parking = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    ratings = models.CharField(max_length=255, blank=True, null=True)
    number_of_ratings = models.CharField(max_length=255, blank=True, null=True)
    categories = models.CharField(max_length=255, blank=True, null=True)
    link_to_menu = models.CharField(max_length=255, blank=True, null=True)
    alcohol = models.CharField(max_length=255, blank=True, null=True)
    breakfast = models.CharField(max_length=255, blank=True, null=True)
    lunch = models.CharField(max_length=255, blank=True, null=True)
    dinner = models.CharField(max_length=255, blank=True, null=True)
    credit_cards = models.CharField(max_length=255, blank=True, null=True)
    credit_card_details = models.CharField(max_length=255, blank=True, null=True)
    good_for_kids = models.CharField(max_length=255, blank=True, null=True)
    childrens_menu = models.CharField(max_length=255, blank=True, null=True)
    takeout = models.CharField(max_length=255, blank=True, null=True)
    delivery = models.CharField(max_length=255, blank=True, null=True)
    kosher = models.CharField(max_length=255, blank=True, null=True)
    halal = models.CharField(max_length=255, blank=True, null=True)
    veganvegetarian = models.CharField(max_length=255, blank=True, null=True)
    gluten_free_options = models.CharField(max_length=255, blank=True, null=True)
    healthy_options = models.CharField(max_length=255, blank=True, null=True)
    low_fat_options = models.CharField(max_length=255, blank=True, null=True)
    low_salt_options = models.CharField(max_length=255, blank=True, null=True)
    organic_options = models.CharField(max_length=255, blank=True, null=True)
    wheelchair_access = models.CharField(max_length=255, blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    open_24_hours = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    chef = models.CharField(max_length=255, blank=True, null=True)
    owner = models.CharField(max_length=255, blank=True, null=True)
    founded = models.CharField(max_length=255, blank=True, null=True)
    reservations = models.CharField(max_length=255, blank=True, null=True)
    private_room = models.CharField(max_length=255, blank=True, null=True)
    catering = models.CharField(max_length=255, blank=True, null=True)
    link_to_yahoo_local = models.CharField(max_length=255, blank=True, null=True)
    link_to_yelp = models.CharField(max_length=255, blank=True, null=True)
    link_to_zagat = models.CharField(max_length=255, blank=True, null=True)
    link_to_opentable = models.CharField(max_length=255, blank=True, null=True)
    link_to_urbanspoon = models.CharField(max_length=255, blank=True, null=True)
    link_to_citysearch = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_eats'


class AbFeatures(models.Model):
    item_id = models.BigIntegerField(blank=True, null=True)
    catcode = models.CharField(max_length=16, blank=True, null=True)
    approved = models.CharField(max_length=1, blank=True, null=True)
    expires = models.DateField(blank=True, null=True)
    extra_order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_features'


class AbFeedContent(models.Model):
    id = models.BigIntegerField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    feed_title = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_feed_content'


class AbFeeds(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    feed_url = models.CharField(unique=True, max_length=255, blank=True, null=True)
    handle = models.CharField(max_length=50, blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    visible = models.CharField(max_length=1, blank=True, null=True)
    created_on = models.DateTimeField()
    feed_content = models.TextField(blank=True, null=True)
    feed_title = models.CharField(max_length=255, blank=True, null=True)
    title_only = models.CharField(max_length=1, blank=True, null=True)
    img_only = models.CharField(max_length=1, blank=True, null=True)
    uid = models.BigIntegerField(primary_key=True)
    last_retrieved = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ab_feeds'


class AbGroupUsers(models.Model):
    gid = models.IntegerField(primary_key=True)
    uid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_group_users'


class AbGroups(models.Model):
    gid = models.IntegerField(primary_key=True)
    group_name = models.CharField(max_length=32, blank=True, null=True)
    descrip = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_groups'


class AbImages(models.Model):
    item_id = models.BigIntegerField(blank=True, null=True)
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.
    effective_date = models.DateField(blank=True, null=True)
    caption = models.CharField(max_length=255, blank=True, null=True)
    credits = models.CharField(max_length=255, blank=True, null=True)
    owner = models.BigIntegerField(blank=True, null=True)
    security_level = models.IntegerField(blank=True, null=True)
    uid = models.BigIntegerField(primary_key=True)
    ext = models.CharField(max_length=5, blank=True, null=True)
    imgcode = models.CharField(max_length=16, blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_images'


class AbItemTypes(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    tablename = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_item_types'


class AbLocation(models.Model):
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    msa = models.CharField(max_length=5, blank=True, null=True)
    fips = models.CharField(db_column='FIPS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(max_length=3, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_location'


class AbPendingEdits(models.Model):
    item_id = models.BigIntegerField(blank=True, null=True)
    new_cid = models.BigIntegerField(blank=True, null=True)
    new_name = models.CharField(max_length=255, blank=True, null=True)
    new_itemcode = models.CharField(max_length=16, blank=True, null=True)
    new_owner = models.BigIntegerField(blank=True, null=True)
    new_effective_date = models.DateField(blank=True, null=True)
    new_url = models.CharField(max_length=255, blank=True, null=True)
    new_content = models.TextField(blank=True, null=True)
    new_security_level = models.IntegerField(blank=True, null=True)
    new_addr = models.CharField(max_length=255, blank=True, null=True)
    new_zip = models.CharField(max_length=15, blank=True, null=True)
    new_phone = models.CharField(max_length=15, blank=True, null=True)
    new_email = models.CharField(max_length=50, blank=True, null=True)
    new_city = models.CharField(max_length=25, blank=True, null=True)
    new_zip4 = models.CharField(max_length=10, blank=True, null=True)
    more_edit_types = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_pending_edits'


class AbPrivate(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_private'


class AbSchool(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    school_type = models.CharField(max_length=1, blank=True, null=True)
    district = models.CharField(max_length=128, blank=True, null=True)
    from_grade = models.IntegerField(blank=True, null=True)
    to_grade = models.IntegerField(blank=True, null=True)
    administrator = models.CharField(max_length=128, blank=True, null=True)
    grades = models.CharField(max_length=24, blank=True, null=True)
    degrees = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_school'


class AbUserFriends(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    friend_id = models.IntegerField(blank=True, null=True)
    access_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_user_friends'


class AbUsersCats(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    cathome = models.BigIntegerField(blank=True, null=True)
    catlast = models.BigIntegerField(blank=True, null=True)
    public_handle = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ab_users_cats'


class BizArizona(models.Model):
    bizid = models.IntegerField(db_column='bizID')  # Field name made lowercase.
    bizcat = models.CharField(db_column='bizCat', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizcatsub = models.CharField(db_column='bizCatSub', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizname = models.CharField(db_column='bizName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizaddr = models.CharField(db_column='bizAddr', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizcity = models.CharField(db_column='bizCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizstate = models.CharField(db_column='bizState', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizzip = models.CharField(db_column='bizZip', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizphone = models.CharField(db_column='bizPhone', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizfax = models.CharField(db_column='bizFax', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizemail = models.CharField(db_column='bizEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    bizurl = models.CharField(db_column='bizURL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    locareacode = models.CharField(db_column='locAreaCode', max_length=3, blank=True, null=True)  # Field name made lowercase.
    locfips = models.CharField(db_column='locFIPS', max_length=5, blank=True, null=True)  # Field name made lowercase.
    loctimezone = models.CharField(db_column='locTimeZone', max_length=6, blank=True, null=True)  # Field name made lowercase.
    locdst = models.CharField(db_column='locDST', max_length=1, blank=True, null=True)  # Field name made lowercase.
    loclat = models.CharField(db_column='locLat', max_length=10, blank=True, null=True)  # Field name made lowercase.
    loclong = models.CharField(db_column='locLong', max_length=10, blank=True, null=True)  # Field name made lowercase.
    locmsa = models.CharField(db_column='locMSA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    locpmsa = models.CharField(db_column='locPMSA', max_length=5, blank=True, null=True)  # Field name made lowercase.
    loccounty = models.CharField(db_column='locCounty', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'biz_arizona'


class BizdirUsers(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    address = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=30, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    ext = models.CharField(max_length=5, blank=True, null=True)
    fax = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=45, blank=True, null=True)
    why = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    admin = models.CharField(max_length=1, blank=True, null=True)
    expires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bizdir_users'


class Content(models.Model):
    id = models.BigIntegerField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    acl = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'content'


class Coordinators(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    altphone = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coordinators'


class Countries(models.Model):
    iso = models.CharField(max_length=2)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'countries'


class Edwardsblog(models.Model):
    who = models.CharField(max_length=16, blank=True, null=True)
    location = models.CharField(max_length=64, blank=True, null=True)
    didit = models.TextField(blank=True, null=True)
    whoandwhy = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'edwardsblog'


class File(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    template = models.CharField(max_length=128, blank=True, null=True)
    target = models.CharField(max_length=128, blank=True, null=True)
    rules = models.CharField(max_length=16, blank=True, null=True)
    acl = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'file'


class FwixCats(models.Model):
    cid = models.BigIntegerField(blank=True, null=True)
    fwix_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fwix_cats'


class Handles(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    handle = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=1, blank=True, null=True)
    within_cat = models.BigIntegerField(blank=True, null=True)
    catid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'handles'


class Longcontent(models.Model):
    id = models.BigIntegerField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    acl = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'longcontent'


class News(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    editor = models.CharField(max_length=64, blank=True, null=True)
    letters_email = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=32, blank=True, null=True)
    zip = models.CharField(max_length=15, blank=True, null=True)
    news_email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=32, blank=True, null=True)
    fax = models.CharField(max_length=32, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    focus = models.CharField(max_length=32, blank=True, null=True)
    extra = models.CharField(max_length=64, blank=True, null=True)
    url = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'


class Person(models.Model):
    id = models.BigIntegerField()
    propername = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    cellphone = models.CharField(max_length=16, blank=True, null=True)
    fax = models.CharField(max_length=16, blank=True, null=True)
    address1 = models.CharField(max_length=128, blank=True, null=True)
    address2 = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=64, blank=True, null=True)
    zip = models.CharField(max_length=16, blank=True, null=True)
    acl = models.CharField(max_length=4, blank=True, null=True)
    captcha_only = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class RcatdbCategories(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cid = models.BigIntegerField(db_column='CID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    rel_url = models.CharField(db_column='REL_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    catcode = models.CharField(max_length=16, blank=True, null=True)
    lastsubcode = models.IntegerField(blank=True, null=True)
    owner = models.BigIntegerField(blank=True, null=True)
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.
    types = models.CharField(max_length=100, blank=True, null=True)
    security_level = models.IntegerField(blank=True, null=True)
    display_order = models.IntegerField(blank=True, null=True)
    external_uri = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rcatdb_categories'


class RcatdbItems(models.Model):
    id = models.BigIntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cid = models.BigIntegerField(db_column='CID')  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255)  # Field name made lowercase.
    value = models.CharField(db_column='VALUE', max_length=255)  # Field name made lowercase.
    qualifier = models.CharField(db_column='QUALIFIER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    itemcode = models.CharField(max_length=16, blank=True, null=True)
    owner = models.BigIntegerField(blank=True, null=True)
    acl = models.CharField(max_length=4, blank=True, null=True)
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.
    effective_date = models.DateField(blank=True, null=True)
    url = models.CharField(db_column='URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    short_content = models.TextField(blank=True, null=True)
    types = models.CharField(db_column='TYPES', max_length=100, blank=True, null=True)  # Field name made lowercase.
    security_level = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)
    hide_from_front = models.CharField(max_length=1, blank=True, null=True)
    adfree = models.CharField(max_length=1, blank=True, null=True)
    is_feed = models.CharField(max_length=1, blank=True, null=True)
    wide = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rcatdb_items'


class RcatdbRcats(models.Model):
    uid = models.BigIntegerField(db_column='UID', primary_key=True)  # Field name made lowercase.
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    relation = models.CharField(db_column='RELATION', max_length=20)  # Field name made lowercase.
    cat_dest = models.BigIntegerField(db_column='CAT_DEST')  # Field name made lowercase.
    item_dest = models.BigIntegerField(db_column='ITEM_DEST')  # Field name made lowercase.
    qualifier = models.CharField(db_column='QUALIFIER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rcatdb_rcats'


class RcatdbRitems(models.Model):
    uid = models.BigIntegerField(db_column='UID', primary_key=True)  # Field name made lowercase.
    id = models.BigIntegerField(db_column='ID')  # Field name made lowercase.
    relation = models.CharField(db_column='RELATION', max_length=20)  # Field name made lowercase.
    cat_dest = models.BigIntegerField(db_column='CAT_DEST')  # Field name made lowercase.
    item_dest = models.BigIntegerField(db_column='ITEM_DEST')  # Field name made lowercase.
    qualifier = models.CharField(db_column='QUALIFIER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rcatdb_ritems'


class Relatedcontent(models.Model):
    uid = models.BigIntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    acl = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relatedcontent'


class Resources(models.Model):
    catid = models.IntegerField()
    rtype = models.CharField(max_length=100, blank=True, null=True)
    resource = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resources'


class Structure(models.Model):
    catid = models.IntegerField(primary_key=True)
    topic = models.CharField(max_length=1024)
    title = models.CharField(max_length=1024, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    lastupdate = models.DateTimeField()
    catcode = models.CharField(max_length=16, blank=True, null=True)
    lastsubcode = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'structure'


class Students4Edwards(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    first_names = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    email = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=2, blank=True, null=True)
    school = models.CharField(max_length=64, blank=True, null=True)
    title = models.CharField(max_length=64, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    endorse = models.TextField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    url = models.CharField(max_length=64, blank=True, null=True)
    address_line1 = models.CharField(max_length=60, blank=True, null=True)
    address_line2 = models.CharField(max_length=60, blank=True, null=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)
    ld = models.CharField(db_column='LD', max_length=10, blank=True, null=True)  # Field name made lowercase.
    win_site = models.CharField(max_length=1, blank=True, null=True)
    listserv = models.CharField(max_length=1, blank=True, null=True)
    volunteer = models.CharField(max_length=1, blank=True, null=True)
    unidos = models.CharField(max_length=1, blank=True, null=True)
    african_americans = models.CharField(max_length=1, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    entered = models.DateTimeField(db_column='ENTERED')  # Field name made lowercase.
    group1 = models.CharField(max_length=16, blank=True, null=True)
    former_candidate = models.IntegerField(blank=True, null=True)
    origdate = models.DateField(blank=True, null=True)
    dontsendmail = models.CharField(db_column='DONTSENDMAIL', max_length=1, blank=True, null=True)  # Field name made lowercase.
    oktosendmail = models.CharField(db_column='OKTOSENDMAIL', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'students4edwards'


class TempData(models.Model):
    id = models.IntegerField(blank=True, null=True)
    person_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temp_data'


class Users(models.Model):
    login = models.CharField(unique=True, max_length=25)
    pw = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    extra_info = models.CharField(max_length=100)
    tmp_mail = models.CharField(max_length=50)
    access_level = models.IntegerField()
    active = models.CharField(max_length=1)
    email = models.CharField(max_length=64, blank=True, null=True)
    return_url = models.CharField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'


class UsersProfile(models.Model):
    users_id = models.IntegerField(unique=True)
    language = models.CharField(max_length=2)
    address = models.CharField(max_length=50)
    postcode = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, blank=True, null=True)
    province = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=2)
    phone = models.CharField(max_length=50)
    fax = models.CharField(max_length=50)
    homepage = models.CharField(max_length=100)
    notes = models.TextField()
    user_1 = models.CharField(max_length=100)
    user_2 = models.CharField(max_length=100)
    user_3 = models.CharField(max_length=100)
    user_4 = models.CharField(max_length=100)
    last_change = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users_profile'


class Viewprefs(models.Model):
    cid = models.BigIntegerField(blank=True, null=True)
    id = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    viewid = models.BigIntegerField(blank=True, null=True)
    pagetype = models.CharField(max_length=32, blank=True, null=True)
    catcode = models.CharField(max_length=16, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'viewprefs'


class Views(models.Model):
    uid = models.BigIntegerField(blank=True, null=True)
    data_source = models.CharField(max_length=64, blank=True, null=True)
    method = models.CharField(max_length=64, blank=True, null=True)
    template_file = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'views'


class Volunteers(models.Model):
    volid = models.BigIntegerField(primary_key=True)
    stu4ed = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    okfor = models.IntegerField(blank=True, null=True)
    total = models.BigIntegerField(blank=True, null=True)
    vouchfor = models.CharField(max_length=128, blank=True, null=True)
    notes = models.CharField(max_length=128, blank=True, null=True)
    password = models.CharField(max_length=16, blank=True, null=True)
    name = models.CharField(max_length=32, blank=True, null=True)
    last_request = models.DateTimeField(db_column='LAST_REQUEST')  # Field name made lowercase.
    num_assigned = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'volunteers'
