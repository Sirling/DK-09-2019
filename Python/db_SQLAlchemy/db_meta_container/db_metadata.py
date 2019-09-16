# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, Float, ForeignKey, Index, String, Table, Time, text
from sqlalchemy.dialects.mysql import INTEGER, LONGTEXT, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class AccessToken(Base):
    __tablename__ = 'access_token'

    id = Column(INTEGER(11), primary_key=True)
    model_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    status = Column(INTEGER(11), nullable=False)
    value = Column(String(255, 'utf8_unicode_ci'), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False)


class Action(Base):
    __tablename__ = 'action'

    id = Column(INTEGER(11), primary_key=True)
    application_id = Column(ForeignKey('qrlink.id'), index=True)
    preview_image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    content_image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    promo_id = Column(ForeignKey('action.id'), index=True)
    label_icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    label_icon_reversed_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    slug = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    discr = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    preview_description = Column(LONGTEXT)
    color = Column(SMALLINT(6))
    size = Column(SMALLINT(6))
    content_description = Column(LONGTEXT)
    content_note = Column(LONGTEXT)
    conditions_note = Column(LONGTEXT)
    campaign_position = Column(SMALLINT(6))
    description = Column(LONGTEXT)
    type = Column(String(255, 'utf8_unicode_ci'))
    promotion_position = Column(SMALLINT(6))
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    common = Column(TINYINT(1), nullable=False)
    label_icon_pdf_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    promoBlock_id = Column(ForeignKey('promo.id'), index=True)

    application = relationship('Qrlink')
    content_image = relationship('File', primaryjoin='Action.content_image_id == File.id')
    image = relationship('File', primaryjoin='Action.image_id == File.id')
    label_icon = relationship('File', primaryjoin='Action.label_icon_id == File.id')
    label_icon_pdf = relationship('File', primaryjoin='Action.label_icon_pdf_id == File.id')
    label_icon_reversed = relationship('File', primaryjoin='Action.label_icon_reversed_id == File.id')
    preview_image = relationship('File', primaryjoin='Action.preview_image_id == File.id')
    promoBlock = relationship('Promo', primaryjoin='Action.promoBlock_id == Promo.id')
    promo = relationship('Action', remote_side=[id])
    stores = relationship('Store', secondary='campaign_store')


class AdditionalMenu(Base):
    __tablename__ = 'additional_menu'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    subdomain = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    path = Column(String(250, 'utf8_unicode_ci'), nullable=False)


class AdminRole(Base):
    __tablename__ = 'admin_roles'

    id = Column(String(255, 'utf8_unicode_ci'), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'))

    admin_user = relationship('AdminUser', secondary='admin_user_roles')


class AdminUser(Base):
    __tablename__ = 'admin_user'

    id = Column(INTEGER(11), primary_key=True)
    login = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    password = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    is_active = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)


t_admin_user_roles = Table(
    'admin_user_roles', metadata,
    Column('id_user', ForeignKey('admin_user.id'), primary_key=True, nullable=False, index=True),
    Column('id_right', ForeignKey('admin_roles.id'), primary_key=True, nullable=False, index=True)
)


class Animal(Base):
    __tablename__ = 'animal'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class Appeal(Base):
    __tablename__ = 'appeal'

    id = Column(INTEGER(11), primary_key=True)
    store_id = Column(ForeignKey('store.id', ondelete='SET NULL'), index=True)
    zone_id = Column(ForeignKey('zone.id', ondelete='SET NULL'), index=True)
    problem_id = Column(ForeignKey('problem.id', ondelete='SET NULL'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    phone = Column(String(1000, 'utf8_unicode_ci'), nullable=False)
    comment = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    is_feedback = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    problem = relationship('Problem')
    store = relationship('Store')
    zone = relationship('Zone')


class BaseProduct(Base):
    __tablename__ = 'base_product'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    price = Column(INTEGER(11), nullable=False)
    vendor_code = Column(INTEGER(11), nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    product_type = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class CertProduct(BaseProduct):
    __tablename__ = 'cert_product'

    id = Column(ForeignKey('base_product.id', ondelete='CASCADE'), primary_key=True)
    group_id = Column(ForeignKey('product_group.id'), index=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    rating = Column(INTEGER(11), nullable=False)

    group = relationship('ProductGroup')
    image = relationship('File')


class EvTicket(BaseProduct):
    __tablename__ = 'ev_ticket'

    id = Column(ForeignKey('base_product.id', ondelete='CASCADE'), primary_key=True)
    event_id = Column(ForeignKey('ev_event.id', ondelete='SET NULL'), index=True)
    type_id = Column(ForeignKey('ev_ticket_type.id', ondelete='SET NULL'), index=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    stop_at = Column(DateTime, nullable=False)
    is_entrance = Column(TINYINT(1), nullable=False)
    lection_start_at = Column(DateTime, nullable=False)
    lection_ends_at = Column(DateTime, nullable=False)
    total_count = Column(INTEGER(11))
    template = Column(LONGTEXT, nullable=False)
    short_description = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    mastercard_discount = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    mastercard_discount_type = Column(SMALLINT(6))
    mastercard_discount_description = Column(String(255, 'utf8_unicode_ci'))
    is_published = Column(TINYINT(1), nullable=False)

    event = relationship('EvEvent')
    image = relationship('File', primaryjoin='EvTicket.image_id == File.id')
    preview = relationship('File', primaryjoin='EvTicket.preview_id == File.id')
    type = relationship('EvTicketType')


class FoodProduct(BaseProduct):
    __tablename__ = 'food_product'

    id = Column(ForeignKey('base_product.id', ondelete='CASCADE'), primary_key=True)


class BaseProductAudit(Base):
    __tablename__ = 'base_product_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class Basket(Base):
    __tablename__ = 'basket'

    id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(ForeignKey('ticket_user.id', ondelete='CASCADE'), unique=True)
    created_at = Column(DateTime, nullable=False)

    customer = relationship('TicketUser')


class BasketItem(Base):
    __tablename__ = 'basket_item'

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(ForeignKey('base_product.id'), nullable=False, index=True)
    basket_id = Column(ForeignKey('basket.id', ondelete='CASCADE'), nullable=False, index=True)
    quantity = Column(INTEGER(11), nullable=False)
    expires_at = Column(DateTime, nullable=False)
    item_order = Column(INTEGER(11), nullable=False, server_default=text("'0'"))
    price = Column(INTEGER(11), nullable=False)
    metadata_ = Column('metadata', LONGTEXT, comment='(DC2Type:array)')

    basket = relationship('Basket')
    product = relationship('BaseProduct')


class CampaignOffer(Base):
    __tablename__ = 'campaign_offer'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    campaign_id = Column(ForeignKey('action.id'), index=True)
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    campaign = relationship('Action')
    image = relationship('File')


class CampaignProduct(Base):
    __tablename__ = 'campaign_product'

    id = Column(INTEGER(11), primary_key=True)
    campaign_offer_id = Column(ForeignKey('campaign_offer.id'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    campaign_offer = relationship('CampaignOffer')


class CampaignProductVersion(Base):
    __tablename__ = 'campaign_product_version'

    id = Column(INTEGER(11), primary_key=True)
    campaign_product_id = Column(ForeignKey('campaign_product.id'), index=True)
    description = Column(LONGTEXT)
    regular_price = Column(LONGTEXT, nullable=False)
    offer_price = Column(LONGTEXT, nullable=False)
    offer_price_description = Column(String(255, 'utf8_unicode_ci'))
    colors = Column(LONGTEXT, nullable=False, comment='(DC2Type:json_array)')
    position = Column(SMALLINT(6))

    campaign_product = relationship('CampaignProduct')


t_campaign_store = Table(
    'campaign_store', metadata,
    Column('campaign_id', ForeignKey('action.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('store_id', ForeignKey('store.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class City(Base):
    __tablename__ = 'city'

    id = Column(INTEGER(11), primary_key=True)
    prefix = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))

    promos = relationship('Promo', secondary='promo_city')


class ConfirmationCode(Base):
    __tablename__ = 'confirmation_code'

    id = Column(INTEGER(11), primary_key=True)
    identifier = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    code = Column(String(255, 'utf8_unicode_ci'), nullable=False, index=True)
    expires_at = Column(DateTime, nullable=False)
    created_at = Column(DateTime, nullable=False)


class Cv(Base):
    __tablename__ = 'cv'

    id = Column(INTEGER(11), primary_key=True)
    city_id = Column(ForeignKey('city.id', ondelete='SET NULL'), index=True)
    file_id = Column(ForeignKey('file.id'), index=True)
    first_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    last_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    birthday = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    phone = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    link = Column(String(1000, 'utf8_unicode_ci'))
    stores = Column(String(255, 'utf8_unicode_ci'))
    position = Column(String(255, 'utf8_unicode_ci'))
    work_time = Column(String(255, 'utf8_unicode_ci'))
    settlement = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)

    city = relationship('City')
    file = relationship('File')


class EvEvent(Base):
    __tablename__ = 'ev_event'

    id = Column(INTEGER(11), primary_key=True)
    logo_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    picture_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    slug = Column(String(128, 'utf8_unicode_ci'), nullable=False, unique=True)
    full_description = Column(LONGTEXT)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    place = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    address = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    color = Column(SMALLINT(6))
    link = Column(String(255, 'utf8_unicode_ci'))
    size = Column(SMALLINT(6))
    facebook_link = Column(String(255, 'utf8_unicode_ci'))
    rules_reference = Column(String(255, 'utf8_unicode_ci'))
    publish = Column(TINYINT(1), nullable=False)
    lng = Column(String(255, 'utf8_unicode_ci'))
    lat = Column(String(255, 'utf8_unicode_ci'))
    application_id = Column(ForeignKey('qrlink.id'), unique=True)
    promotion_id = Column(ForeignKey('action.id', ondelete='SET NULL'), index=True)
    promotions_title = Column(String(255, 'utf8_unicode_ci'))
    subscription = Column(TINYINT(1), nullable=False)
    picture_content_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    event_position = Column(SMALLINT(6))

    application = relationship('Qrlink')
    logo = relationship('File', primaryjoin='EvEvent.logo_id == File.id')
    picture_content = relationship('File', primaryjoin='EvEvent.picture_content_id == File.id')
    picture = relationship('File', primaryjoin='EvEvent.picture_id == File.id')
    preview = relationship('File', primaryjoin='EvEvent.preview_id == File.id')
    promotion = relationship('Action')


class EvEventAudit(Base):
    __tablename__ = 'ev_event_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class EvTicketAudit(Base):
    __tablename__ = 'ev_ticket_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class EvTicketType(Base):
    __tablename__ = 'ev_ticket_type'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class EvTicketTypeAudit(Base):
    __tablename__ = 'ev_ticket_type_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class EventProperty(Base):
    __tablename__ = 'event_property'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    event_id = Column(ForeignKey('ev_event.id'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    position = Column(SMALLINT(6))

    event = relationship('EvEvent')
    image = relationship('File')


class EventPropertyAudit(Base):
    __tablename__ = 'event_property_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class EventReminder(Base):
    __tablename__ = 'event_reminder'
    __table_args__ = (
        Index('UNIQ_6DBA69071F7E88BE7927C74444F97DD', 'event_id', 'email', 'phone', unique=True),
    )

    id = Column(INTEGER(11), primary_key=True)
    event_id = Column(ForeignKey('ev_event.id'), index=True)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    phone = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)

    event = relationship('EvEvent')


class EventSchedule(Base):
    __tablename__ = 'event_schedule'

    id = Column(INTEGER(11), primary_key=True)
    event_id = Column(ForeignKey('ev_event.id'), index=True)
    title = Column(LONGTEXT, nullable=False)
    description = Column(LONGTEXT)
    position = Column(SMALLINT(6))

    event = relationship('EvEvent')


class Faqcategory(Base):
    __tablename__ = 'faqcategory'

    id = Column(INTEGER(11), primary_key=True)
    icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    icon = relationship('File')


class Faqquestion(Base):
    __tablename__ = 'faqquestion'

    id = Column(INTEGER(11), primary_key=True)
    category_id = Column(ForeignKey('faqcategory.id'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    vote_positive = Column(INTEGER(11), nullable=False)
    vote_negative = Column(INTEGER(11), nullable=False)
    position = Column(SMALLINT(6))

    category = relationship('Faqcategory')


class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(INTEGER(11), primary_key=True)
    subject_id = Column(ForeignKey('feedback_subject.id', ondelete='SET NULL'), index=True)
    file_id = Column(ForeignKey('file.id'), index=True)
    subject_title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    phone = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    content = Column(LONGTEXT, nullable=False)
    barcode = Column(String(255, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    file = relationship('File')
    subject = relationship('FeedbackSubject')


class FeedbackSubject(Base):
    __tablename__ = 'feedback_subject'

    id = Column(INTEGER(11), primary_key=True)
    feedbackSubjectId = Column(INTEGER(11), nullable=False)
    subjectUa = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    subjectRu = Column(String(255, 'utf8_unicode_ci'))
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))


class File(Base):
    __tablename__ = 'file'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    size = Column(INTEGER(11), nullable=False)
    path = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    uploaded_at = Column(DateTime, nullable=False)
    file_type = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class FooterActionLink(Base):
    __tablename__ = 'footer_action_link'

    id = Column(INTEGER(11), primary_key=True)
    action_id = Column(ForeignKey('action.id', ondelete='CASCADE'), index=True)
    position = Column(SMALLINT(6))

    action = relationship('Action')


class FooterLabel(Base):
    __tablename__ = 'footer_label'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    type = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class FooterStaticPageLink(Base):
    __tablename__ = 'footer_static_page_link'

    id = Column(INTEGER(11), primary_key=True)
    page_id = Column(ForeignKey('page.id', ondelete='CASCADE'), index=True)
    position = Column(SMALLINT(6))

    page = relationship('Page')


class Habit(Base):
    __tablename__ = 'habit'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class HrAdvantage(Base):
    __tablename__ = 'hr_advantage'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    template_id = Column(ForeignKey('hr_template.id'), index=True)
    page_id = Column(ForeignKey('hr_page.id'), index=True)
    vacancy_id = Column(ForeignKey('hr_vacancy.id'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    position = Column(SMALLINT(6))

    image = relationship('File')
    page = relationship('HrPage')
    template = relationship('HrTemplate')
    vacancy = relationship('HrVacancy')


class HrAdvantageAudit(Base):
    __tablename__ = 'hr_advantage_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class HrBaseResp(Base):
    __tablename__ = 'hr_base_resp'

    id = Column(INTEGER(11), primary_key=True)
    template_id = Column(ForeignKey('hr_template.id'), index=True)
    vacancy_id = Column(ForeignKey('hr_vacancy.id'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))
    discr = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    template = relationship('HrTemplate')
    vacancy = relationship('HrVacancy')


class HrBaseRespAudit(Base):
    __tablename__ = 'hr_base_resp_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)
    discr = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class HrCondition(Base):
    __tablename__ = 'hr_condition'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    main_page_id = Column(ForeignKey('hr_main_page.id'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    position = Column(SMALLINT(6))

    image = relationship('File')
    main_page = relationship('HrMainPage')


class HrEmailDirectory(Base):
    __tablename__ = 'hr_email_directory'

    id = Column(INTEGER(11), primary_key=True)
    region_id = Column(INTEGER(11), nullable=False)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class HrMainPage(Base):
    __tablename__ = 'hr_main_page'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    img_block_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_small_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_middle_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_full_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    color = Column(SMALLINT(6))
    description = Column(LONGTEXT)
    form_title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    video = Column(String(255, 'utf8_unicode_ci'))

    image = relationship('File', primaryjoin='HrMainPage.image_id == File.id')
    img_block = relationship('File', primaryjoin='HrMainPage.img_block_id == File.id')
    preview_full = relationship('File', primaryjoin='HrMainPage.preview_full_id == File.id')
    preview_middle = relationship('File', primaryjoin='HrMainPage.preview_middle_id == File.id')
    preview_small = relationship('File', primaryjoin='HrMainPage.preview_small_id == File.id')


class HrOffice(Base):
    __tablename__ = 'hr_office'

    id = Column(INTEGER(11), primary_key=True)
    city_id = Column(ForeignKey('city.id', ondelete='SET NULL'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    address = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    city = relationship('City')


class HrOfficeAudit(Base):
    __tablename__ = 'hr_office_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class HrPage(Base):
    __tablename__ = 'hr_page'

    id = Column(INTEGER(11), primary_key=True)
    header_icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    body_image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    promo1_id = Column(ForeignKey('promo.id'), index=True)
    promo2_id = Column(ForeignKey('promo.id'), index=True)
    preview_small_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_middle_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_full_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    is_published = Column(TINYINT(1), nullable=False)
    slug = Column(String(128, 'utf8_unicode_ci'), nullable=False, unique=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT, nullable=False)
    header_color = Column(SMALLINT(6))
    anket_type = Column(SMALLINT(6))
    form_title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    show_in_block = Column(TINYINT(1), nullable=False)
    show_in_menu = Column(TINYINT(1), nullable=False)
    ambasador_emails = Column(String(255, 'utf8_unicode_ci'))
    vacancy_title = Column(String(255, 'utf8_unicode_ci'))
    video = Column(String(255, 'utf8_unicode_ci'))

    body_image = relationship('File', primaryjoin='HrPage.body_image_id == File.id')
    header_icon = relationship('File', primaryjoin='HrPage.header_icon_id == File.id')
    preview_full = relationship('File', primaryjoin='HrPage.preview_full_id == File.id')
    preview_middle = relationship('File', primaryjoin='HrPage.preview_middle_id == File.id')
    preview_small = relationship('File', primaryjoin='HrPage.preview_small_id == File.id')
    promo1 = relationship('Promo', primaryjoin='HrPage.promo1_id == Promo.id')
    promo2 = relationship('Promo', primaryjoin='HrPage.promo2_id == Promo.id')
    vacancys = relationship('HrVacancy', secondary='vacancy_page')


class HrPosition(Base):
    __tablename__ = 'hr_position'

    id = Column(INTEGER(11), primary_key=True)
    slug = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)


class HrSelStage(Base):
    __tablename__ = 'hr_sel_stage'

    id = Column(INTEGER(11), primary_key=True)
    template_id = Column(ForeignKey('hr_template.id'), index=True)
    page_id = Column(ForeignKey('hr_page.id'), index=True)
    vacancy_id = Column(ForeignKey('hr_vacancy.id'), index=True)
    description = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    page = relationship('HrPage')
    template = relationship('HrTemplate')
    vacancy = relationship('HrVacancy')


class HrSelStageAudit(Base):
    __tablename__ = 'hr_sel_stage_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class HrSlide(Base):
    __tablename__ = 'hr_slide'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    main_page_id = Column(ForeignKey('hr_main_page.id'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    image = relationship('File')
    main_page = relationship('HrMainPage')


class HrTemplate(Base):
    __tablename__ = 'hr_template'

    id = Column(INTEGER(11), primary_key=True)
    position_id = Column(ForeignKey('hr_position.id'), index=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    type = Column(SMALLINT(6), nullable=False, server_default=text("'1'"))
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    rubric = Column(INTEGER(11), nullable=False)
    category = Column(INTEGER(11), nullable=False)
    responcebilities_title = Column(String(255, 'utf8_unicode_ci'))
    requirements_title = Column(String(255, 'utf8_unicode_ci'))
    form_title = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    image = relationship('File')
    position = relationship('HrPosition')


class HrTemplateAudit(Base):
    __tablename__ = 'hr_template_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class HrVacancy(Base):
    __tablename__ = 'hr_vacancy'

    id = Column(INTEGER(11), primary_key=True)
    position_id = Column(ForeignKey('hr_position.id'), index=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    city_id = Column(ForeignKey('city.id', ondelete='SET NULL'), index=True)
    office_id = Column(ForeignKey('hr_office.id', ondelete='SET NULL'), index=True)
    store_id = Column(ForeignKey('store.id', ondelete='SET NULL'), index=True)
    template_id = Column(ForeignKey('hr_template.id'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    type = Column(SMALLINT(6), nullable=False, server_default=text("'1'"))
    employment = Column(SMALLINT(6), nullable=False)
    is_published = Column(TINYINT(1), nullable=False)
    is_experienced = Column(TINYINT(1), nullable=False)
    contact_one = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    contact_two = Column(String(255, 'utf8_unicode_ci'))
    manager_name = Column(String(255, 'utf8_unicode_ci'))
    reward = Column(String(255, 'utf8_unicode_ci'))
    is_delivery = Column(TINYINT(1), nullable=False)
    is_disability = Column(TINYINT(1), nullable=False)
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    form_title = Column(String(255, 'utf8_unicode_ci'))
    responcebilities_title = Column(String(255, 'utf8_unicode_ci'))
    requirements_title = Column(String(255, 'utf8_unicode_ci'))
    rubric = Column(INTEGER(11), nullable=False)
    category = Column(INTEGER(11), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    address = Column(String(255, 'utf8_unicode_ci'))

    city = relationship('City')
    image = relationship('File')
    office = relationship('HrOffice')
    position = relationship('HrPosition')
    store = relationship('Store')
    template = relationship('HrTemplate')


class HrVacancyAudit(Base):
    __tablename__ = 'hr_vacancy_audit'

    id = Column(INTEGER(10), primary_key=True)
    type = Column(String(10, 'utf8_unicode_ci'), nullable=False, index=True)
    object_id = Column(INTEGER(10), nullable=False, index=True)
    diffs = Column(LONGTEXT, comment='(DC2Type:json_array)')
    blame_id = Column(INTEGER(10), index=True)
    blame_user = Column(String(100, 'utf8_unicode_ci'))
    ip = Column(String(45, 'utf8_unicode_ci'))
    created_at = Column(DateTime, nullable=False, index=True)


class Image(Base):
    __tablename__ = 'images'

    id = Column(String(255, 'utf8_unicode_ci'), primary_key=True)
    path = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    mime_type = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    size = Column(INTEGER(11), nullable=False)
    uploaded_at = Column(DateTime, nullable=False)


class Label(Base):
    __tablename__ = 'label'

    id = Column(INTEGER(11), primary_key=True)
    icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'))
    description = Column(LONGTEXT)

    icon = relationship('File')


class Link(Base):
    __tablename__ = 'link'

    id = Column(INTEGER(11), primary_key=True)
    additional_menu_id = Column(ForeignKey('additional_menu.id'), index=True)
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    path = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    tag_ga = Column(String(250, 'utf8_unicode_ci'))
    position = Column(SMALLINT(6))

    additional_menu = relationship('AdditionalMenu')


class Log(Base):
    __tablename__ = 'log'

    id = Column(INTEGER(11), primary_key=True)
    message = Column(LONGTEXT, nullable=False)
    channel = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    context = Column(LONGTEXT, nullable=False, comment='(DC2Type:array)')
    level = Column(SMALLINT(6), nullable=False)
    level_name = Column(String(50, 'utf8_unicode_ci'), nullable=False)
    extra = Column(LONGTEXT, nullable=False, comment='(DC2Type:array)')
    created_at = Column(DateTime, nullable=False)


class MacroRegion(Base):
    __tablename__ = 'macro_region'

    id = Column(INTEGER(11), primary_key=True)
    pp_id = Column(INTEGER(11), nullable=False)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class MainList(Base):
    __tablename__ = 'main_list'

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(ForeignKey('product.id'), unique=True)
    promo_id = Column(ForeignKey('promo.id'), unique=True)
    type = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))
    size = Column(SMALLINT(6), server_default=text("'1'"))
    color = Column(SMALLINT(6), server_default=text("'1'"))

    product = relationship('Product')
    promo = relationship('Promo')


class MemberQuestion(Base):
    __tablename__ = 'member_question'

    id = Column(INTEGER(11), primary_key=True)
    barcode = Column(String(255, 'utf8_unicode_ci'), nullable=False, index=True)
    answer = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    question_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    requested_at = Column(DateTime, nullable=False)


class Menu(Base):
    __tablename__ = 'menu'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    path = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    tag_ga = Column(String(250, 'utf8_unicode_ci'))
    position = Column(SMALLINT(6))


class MigrationVersion(Base):
    __tablename__ = 'migration_versions'

    version = Column(String(255, 'utf8_unicode_ci'), primary_key=True)


class MobBanner(Base):
    __tablename__ = 'mob_banner'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    color = Column(SMALLINT(6), nullable=False)
    text = Column(String(150, 'utf8_unicode_ci'), nullable=False)
    link = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    period_start = Column(DateTime)
    period_end = Column(DateTime)

    image = relationship('File')


class Office(Base):
    __tablename__ = 'office'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    lng = Column(String(255, 'utf8_unicode_ci'))
    lat = Column(String(255, 'utf8_unicode_ci'))


class OrderItem(Base):
    __tablename__ = 'order_item'

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(ForeignKey('orders.id', ondelete='CASCADE'), nullable=False, index=True)
    product_id = Column(ForeignKey('base_product.id'), nullable=False, index=True)
    quantity = Column(INTEGER(11), nullable=False)
    price = Column(INTEGER(11), nullable=False)
    metadata_ = Column('metadata', LONGTEXT, comment='(DC2Type:array)')

    order = relationship('Order')
    product = relationship('BaseProduct')


class OrderItemSubItem(Base):
    __tablename__ = 'order_item_sub_item'

    id = Column(INTEGER(11), primary_key=True)
    order_item_id = Column(ForeignKey('order_item.id', ondelete='CASCADE'), nullable=False, index=True)
    code = Column(String(255, 'utf8_unicode_ci'))

    order_item = relationship('OrderItem')


class OrderProxy(Base):
    __tablename__ = 'order_proxy'

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    upc_order_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    type = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_payed = Column(TINYINT(1), nullable=False)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(INTEGER(11), primary_key=True)
    customer_id = Column(ForeignKey('ticket_user.id', ondelete='CASCADE'), index=True)
    created_at = Column(DateTime, nullable=False)
    expires_at = Column(DateTime, nullable=False)
    order_status = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    payed_at = Column(DateTime)

    customer = relationship('TicketUser')


class Page(Base):
    __tablename__ = 'page'

    id = Column(INTEGER(11), primary_key=True)
    type = Column(String(255, 'utf8_unicode_ci'), nullable=False, index=True)
    parent_pages = Column(LONGTEXT, nullable=False, comment='(DC2Type:array)')
    children_pages = Column(LONGTEXT, nullable=False, comment='(DC2Type:array)')
    properties = Column(LONGTEXT, nullable=False, comment='(DC2Type:json_array)')
    application_id = Column(ForeignKey('qrlink.id'), index=True)

    application = relationship('Qrlink')


class PageCv(Base):
    __tablename__ = 'page_cv'

    id = Column(INTEGER(11), primary_key=True)
    page_id = Column(ForeignKey('hr_page.id'), index=True)
    full_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    place_of_residence = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    birthday = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    phone = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    university = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    specialization = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    grade = Column(INTEGER(11), nullable=False)
    grade_point_average = Column(DECIMAL(10, 0))
    additional_education = Column(String(255, 'utf8_unicode_ci'))
    graduate_date = Column(String(255, 'utf8_unicode_ci'))
    previous_work = Column(String(255, 'utf8_unicode_ci'))
    position = Column(String(255, 'utf8_unicode_ci'))
    main_responsibilities = Column(String(255, 'utf8_unicode_ci'))
    work_period = Column(String(255, 'utf8_unicode_ci'))
    in_instagram = Column(TINYINT(1), server_default=text("'0'"))
    in_facebook = Column(TINYINT(1), server_default=text("'0'"))
    in_telegram = Column(TINYINT(1), server_default=text("'0'"))
    other_socials = Column(String(255, 'utf8_unicode_ci'))
    ambasador_participation = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    leadership_qualities = Column(String(255, 'utf8_unicode_ci'))
    team_working = Column(String(255, 'utf8_unicode_ci'))
    disposition_qualities = Column(String(255, 'utf8_unicode_ci'))
    email = Column(String(255, 'utf8_unicode_ci'))

    page = relationship('HrPage')


class Partner(Base):
    __tablename__ = 'partner'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    slug = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)
    content = Column(LONGTEXT)
    link = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    link_title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    color = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    image = relationship('File')


class PartnerContact(Base):
    __tablename__ = 'partner_contact'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    persons = relationship('Person', secondary='partner_contact_person')


t_partner_contact_person = Table(
    'partner_contact_person', metadata,
    Column('person_id', ForeignKey('person.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('partner_contact_id', ForeignKey('partner_contact.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class Payment(Base):
    __tablename__ = 'payments'

    id = Column(INTEGER(11), primary_key=True)
    order_id = Column(ForeignKey('orders.id'), unique=True)
    merchant_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    terminal_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    tran_code = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    currency = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    approval_code = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    signature = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    purchase_time = Column(DateTime, nullable=False)
    total_amount = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    proxy_pan = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    sd = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    xid = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    rrn = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    card = Column(String(15, 'utf8_unicode_ci'))

    order = relationship('Order')


class Person(Base):
    __tablename__ = 'person'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    phones = Column(LONGTEXT, nullable=False, comment='(DC2Type:json_array)')
    emails = Column(LONGTEXT, nullable=False, comment='(DC2Type:json_array)')


class PhoneCode(Base):
    __tablename__ = 'phone_code'

    id = Column(INTEGER(11), primary_key=True)
    code = Column(String(255, 'utf8_unicode_ci'), nullable=False, index=True)
    description = Column(String(255, 'utf8_unicode_ci'))
    type = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class PrStore(Base):
    __tablename__ = 'pr_store'

    id = Column(INTEGER(11), primary_key=True)
    store_id = Column(ForeignKey('store.id', ondelete='SET NULL'), index=True)
    phone = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    store = relationship('Store')
    zones = relationship('Zone', secondary='problem_store_zone')


class PressRelease(Base):
    __tablename__ = 'press_release'

    id = Column(INTEGER(11), primary_key=True)
    background_image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    preview_image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    pdf_file_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(100, 'utf8_unicode_ci'))
    slug = Column(String(255, 'utf8_unicode_ci'))
    content = Column(LONGTEXT)
    preview_description = Column(LONGTEXT)
    fb_link = Column(String(255, 'utf8_unicode_ci'))
    twitter_link = Column(String(255, 'utf8_unicode_ci'))
    selected = Column(TINYINT(1), nullable=False)
    published_at = Column(DateTime, nullable=False)
    published = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)

    background_image = relationship('File', primaryjoin='PressRelease.background_image_id == File.id')
    pdf_file = relationship('File', primaryjoin='PressRelease.pdf_file_id == File.id')
    preview_image = relationship('File', primaryjoin='PressRelease.preview_image_id == File.id')


class PrivateUser(Base):
    __tablename__ = 'private_user'

    id = Column(INTEGER(11), primary_key=True)
    firstName = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    lastName = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    middleName = Column(String(255, 'utf8_unicode_ci'))
    email = Column(String(255, 'utf8_unicode_ci'))
    emailConfirmed = Column(TINYINT(1), nullable=False)
    notification = Column(String(255, 'utf8_unicode_ci'))
    bonusAmount = Column(INTEGER(11), nullable=False)
    vouchersAmount = Column(Float(asdecimal=True), nullable=False)
    updatedAt = Column(DateTime, nullable=False)
    createAt = Column(DateTime, nullable=False)
    checkedAt = Column(DateTime, nullable=False)
    spawnNextCouponAt = Column(DateTime)
    barcode = Column(String(255, 'utf8_unicode_ci'))
    fullPhoneNumber = Column(String(255, 'utf8_unicode_ci'))
    balance = Column(INTEGER(11))


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    is_feedback = Column(TINYINT(1), nullable=False)
    is_sendSms = Column(TINYINT(1), nullable=False)
    is_hotline = Column(TINYINT(1), nullable=False)
    is_comment = Column(TINYINT(1), nullable=False)
    position = Column(SMALLINT(6))


t_problem_store_zone = Table(
    'problem_store_zone', metadata,
    Column('problem_store_id', ForeignKey('pr_store.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('zone_id', ForeignKey('zone.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class Product(Base):
    __tablename__ = 'product'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    label_id = Column(ForeignKey('label.id'), unique=True)
    promotion_id = Column(ForeignKey('action.id', ondelete='SET NULL'), index=True)
    category_id = Column(ForeignKey('product_category.id', ondelete='SET NULL'), index=True)
    articul = Column(INTEGER(11))
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    slug = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)
    weight = Column(String(255, 'utf8_unicode_ci'))
    color = Column(SMALLINT(6))
    size = Column(SMALLINT(6))
    price = Column(String(255, 'utf8_unicode_ci'))
    old_price = Column(String(255, 'utf8_unicode_ci'))
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    position = Column(SMALLINT(6))
    priority = Column(INTEGER(11), nullable=False)
    discount = Column(String(255, 'utf8_unicode_ci'))
    type = Column(SMALLINT(6), nullable=False, server_default=text("'1'"))
    points = Column(String(255, 'utf8_unicode_ci'))
    points_text = Column(String(255, 'utf8_unicode_ci'))
    properties_block_title = Column(String(255, 'utf8_unicode_ci'))
    properties_block_description = Column(LONGTEXT)
    image_url = Column(String(255, 'utf8_unicode_ci'))

    category = relationship('ProductCategory')
    image = relationship('File')
    label = relationship('Label')
    promotion = relationship('Action')
    stores = relationship('Store', secondary='product_store')


class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(INTEGER(11), primary_key=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    position = Column(SMALLINT(6))
    md_id = Column(INTEGER(11), nullable=False)


class ProductGroup(Base):
    __tablename__ = 'product_group'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    size = Column(SMALLINT(6))
    is_active = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    start_at = Column(DateTime, nullable=False)
    end_at = Column(DateTime, nullable=False)
    full_description = Column(LONGTEXT)
    priority = Column(INTEGER(11), nullable=False)
    is_published = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    group_id = Column(INTEGER(11))

    image = relationship('File')


class ProductProperty(Base):
    __tablename__ = 'product_property'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    product_id = Column(ForeignKey('product.id'), index=True)
    description = Column(LONGTEXT)
    position = Column(SMALLINT(6))

    image = relationship('File')
    product = relationship('Product')


t_product_store = Table(
    'product_store', metadata,
    Column('product_id', ForeignKey('product.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('store_id', ForeignKey('store.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class Promo(Base):
    __tablename__ = 'promo'

    id = Column(INTEGER(11), primary_key=True)
    image_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    promotion_id = Column(ForeignKey('action.id', ondelete='CASCADE'), index=True)
    campaign_id = Column(ForeignKey('action.id', ondelete='CASCADE'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    description = Column(LONGTEXT)
    color = Column(SMALLINT(6))
    type = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    link = Column(String(255, 'utf8_unicode_ci'))
    size = Column(SMALLINT(6), server_default=text("'3'"))
    period_start = Column(DateTime)
    period_end = Column(DateTime)
    image_small_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    image_full_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    image_middle_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    display_type = Column(SMALLINT(6), server_default=text("'1'"))
    video = Column(String(255, 'utf8_unicode_ci'))
    details_button = Column(TINYINT(1), nullable=False)
    location_display_type = Column(SMALLINT(6), server_default=text("'1'"))

    campaign = relationship('Action', primaryjoin='Promo.campaign_id == Action.id')
    image_full = relationship('File', primaryjoin='Promo.image_full_id == File.id')
    image = relationship('File', primaryjoin='Promo.image_id == File.id')
    image_middle = relationship('File', primaryjoin='Promo.image_middle_id == File.id')
    image_small = relationship('File', primaryjoin='Promo.image_small_id == File.id')
    promotion = relationship('Action', primaryjoin='Promo.promotion_id == Action.id')
    stores = relationship('Store', secondary='promo_store')


class PromoBlock(Base):
    __tablename__ = 'promo_block'

    id = Column(INTEGER(11), primary_key=True)
    promo_id = Column(ForeignKey('promo.id'), index=True)
    promo_page_id = Column(ForeignKey('promo_page.id'), index=True)
    position = Column(SMALLINT(6))

    promo = relationship('Promo')
    promo_page = relationship('PromoPage')


t_promo_city = Table(
    'promo_city', metadata,
    Column('promo_id', ForeignKey('promo.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('city_id', ForeignKey('city.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class PromoPage(Base):
    __tablename__ = 'promo_page'

    id = Column(INTEGER(11), primary_key=True)
    page_id = Column(ForeignKey('page.id'), index=True)
    action_id = Column(ForeignKey('action.id'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    type = Column(SMALLINT(6), nullable=False, server_default=text("'1'"))

    action = relationship('Action')
    page = relationship('Page')


t_promo_store = Table(
    'promo_store', metadata,
    Column('promo_id', ForeignKey('promo.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('store_id', ForeignKey('store.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class PromotionProduct(Base):
    __tablename__ = 'promotion_product'

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(ForeignKey('product.id', ondelete='CASCADE'), unique=True)
    label_icon = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    color = Column(SMALLINT(6), nullable=False)
    size = Column(SMALLINT(6), nullable=False)

    product = relationship('Product')


class Qrlink(Base):
    __tablename__ = 'qrlink'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    qr_google_play_link = Column(LONGTEXT)
    qr_app_store_link = Column(LONGTEXT)
    app_store_link_source = Column(LONGTEXT)
    google_play_link_source = Column(LONGTEXT)
    slug = Column(String(128, 'utf8_unicode_ci'), nullable=False, unique=True)
    description = Column(String(255, 'utf8_unicode_ci'), nullable=False, server_default=text("'promo text'"))


class ShortUrl(Base):
    __tablename__ = 'short_url'

    id = Column(String(255, 'utf8_unicode_ci'), primary_key=True)
    url = Column(LONGTEXT, nullable=False)
    created_at = Column(DateTime)


class SkuLagerInfo(Base):
    __tablename__ = 'sku_lager_info'

    id = Column(INTEGER(11), primary_key=True)
    product_id = Column(ForeignKey('product.id'), unique=True)
    lager = Column(INTEGER(11), nullable=False, unique=True)
    sku_name_ua = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    unit = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    price = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    photo_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    kolvo_state = Column(INTEGER(11), nullable=False)
    parameters = Column(LONGTEXT, nullable=False, comment='(DC2Type:json_array)')
    group_id = Column(INTEGER(11), nullable=False)
    labels = Column(LONGTEXT, nullable=False, comment='(DC2Type:json_array)')

    product = relationship('Product')


class SocialNetwork(Base):
    __tablename__ = 'social_network'

    id = Column(INTEGER(11), primary_key=True)
    icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    link = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    icon = relationship('File')


class Store(Base):
    __tablename__ = 'store'

    id = Column(INTEGER(11), primary_key=True)
    city_id = Column(ForeignKey('city.id', ondelete='SET NULL'), index=True)
    filial_id = Column(INTEGER(11))
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    slug = Column(String(255, 'utf8_unicode_ci'), nullable=False, unique=True)
    open_at = Column(Time)
    close_at = Column(Time)
    lng = Column(String(255, 'utf8_unicode_ci'))
    lat = Column(String(255, 'utf8_unicode_ci'))
    premium = Column(TINYINT(1), nullable=False)
    has_certificate = Column(TINYINT(1), nullable=False)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    street_type_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    street_name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    filial_house = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    macro_region_id = Column(ForeignKey('macro_region.id'), index=True)
    market_status_id = Column(INTEGER(11), nullable=False)
    mobile_phone_number = Column(String(255, 'utf8_unicode_ci'))
    filial_type = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    city = relationship('City')
    macro_region = relationship('MacroRegion')


class StoreDayLoad(Base):
    __tablename__ = 'store_day_load'

    id = Column(INTEGER(11), primary_key=True)
    store_id = Column(ForeignKey('store.id'), index=True)
    dayCode = Column(INTEGER(11), nullable=False)
    fromHour = Column(INTEGER(11), nullable=False)
    toHour = Column(INTEGER(11), nullable=False)
    traffic = Column(INTEGER(11), nullable=False)

    store = relationship('Store')


class StoreService(Base):
    __tablename__ = 'store_service'

    id = Column(INTEGER(11), primary_key=True)
    icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)

    icon = relationship('File')


class StoreServiceMap(Base):
    __tablename__ = 'store_service_map'

    id = Column(INTEGER(11), primary_key=True)
    store_id = Column(ForeignKey('store.id', ondelete='CASCADE'), index=True)
    service_id = Column(ForeignKey('store_service.id', ondelete='CASCADE'), index=True)
    enabled = Column(TINYINT(1), nullable=False)

    service = relationship('StoreService')
    store = relationship('Store')


class SubLink(Base):
    __tablename__ = 'sub_link'

    id = Column(INTEGER(11), primary_key=True)
    menu_id = Column(ForeignKey('menu.id'), index=True)
    link_id = Column(ForeignKey('link.id'), index=True)
    title = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    path = Column(String(250, 'utf8_unicode_ci'), nullable=False)
    tag_ga = Column(String(250, 'utf8_unicode_ci'))
    position = Column(SMALLINT(6))

    link = relationship('Link')
    menu = relationship('Menu')


class Succes(Base):
    __tablename__ = 'success'

    id = Column(INTEGER(11), primary_key=True)
    merchant_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    terminal_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    tran_code = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    currency = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    approval_code = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    order_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    signature = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    purchase_time = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    total_amount = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    proxy_pan = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    sd = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    xid = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    rrn = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    email = Column(String(255, 'utf8_unicode_ci'), nullable=False)


class Term(Base):
    __tablename__ = 'terms'

    id = Column(INTEGER(11), primary_key=True)
    icon_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    campaign_id = Column(ForeignKey('action.id', ondelete='CASCADE'), index=True)
    title = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    position = Column(SMALLINT(6))

    campaign = relationship('Action')
    icon = relationship('File')


class TicketToken(Base):
    __tablename__ = 'ticket_token'

    id = Column(INTEGER(11), primary_key=True)
    model_id = Column(String(255, 'utf8_unicode_ci'), nullable=False)
    status = Column(INTEGER(11), nullable=False)
    value = Column(String(255, 'utf8_unicode_ci'), nullable=False, index=True)
    created_at = Column(DateTime, nullable=False)


class TicketUser(Base):
    __tablename__ = 'ticket_user'

    id = Column(INTEGER(11), primary_key=True)
    phone = Column(String(255, 'utf8_unicode_ci'), unique=True)
    created_at = Column(DateTime, nullable=False)
    name = Column(String(255, 'utf8_unicode_ci'))
    email = Column(String(255, 'utf8_unicode_ci'), unique=True)
    send_to_email = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    card = Column(String(255, 'utf8_unicode_ci'))


class UpdateFromFile(Base):
    __tablename__ = 'update_from_file'

    id = Column(INTEGER(11), primary_key=True)
    file_id = Column(ForeignKey('file.id', ondelete='SET NULL'), index=True)
    promotion_id = Column(ForeignKey('action.id', ondelete='CASCADE'), unique=True)
    update_at = Column(DateTime, nullable=False)

    file = relationship('File')
    promotion = relationship('Action')


t_vacancy_page = Table(
    'vacancy_page', metadata,
    Column('vacancy_id', ForeignKey('hr_vacancy.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True),
    Column('page_id', ForeignKey('hr_page.id', ondelete='CASCADE'), primary_key=True, nullable=False, index=True)
)


class WbntDfgbTest(Base):
    __tablename__ = 'wbnt_dfgb_test'

    id = Column(INTEGER(11), primary_key=True)
    testrelated_id = Column(ForeignKey('wbnt_dfgb_testrelated.id', ondelete='CASCADE'), index=True)
    name = Column(String(60, 'utf8_unicode_ci'))

    testrelated = relationship('WbntDfgbTestrelated')


class WbntDfgbTestrelated(Base):
    __tablename__ = 'wbnt_dfgb_testrelated'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(60, 'utf8_unicode_ci'))


class Workflow(Base):
    __tablename__ = 'workflow'

    flow_id = Column(INTEGER(11), primary_key=True)
    access_code_id = Column(INTEGER(11))
    current_place = Column(LONGTEXT, comment='(DC2Type:array)')
    phone = Column(String(255, 'utf8_unicode_ci'))
    email = Column(String(255, 'utf8_unicode_ci'))
    loyalty_card = Column(String(13, 'utf8_unicode_ci'))
    registarte_data = Column(LONGTEXT, comment='(DC2Type:array)')
    access_email_id = Column(INTEGER(11))


class Zone(Base):
    __tablename__ = 'zone'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255, 'utf8_unicode_ci'), nullable=False)
