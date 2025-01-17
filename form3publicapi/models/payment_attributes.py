# -*- coding: utf-8 -*-

"""
form3publicapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from form3publicapi.api_helper import APIHelper
from form3publicapi.models.agent import Agent
from form3publicapi.models.beneficiary_party_1 import BeneficiaryParty1
from form3publicapi.models.charges_information import ChargesInformation
from form3publicapi.models.debtor_party import DebtorParty
from form3publicapi.models.fx import Fx
from form3publicapi.models.intermediary_bank_account_holding_entity import IntermediaryBankAccountHoldingEntity
from form3publicapi.models.receivers_correspondent_account_holding_entity import ReceiversCorrespondentAccountHoldingEntity
from form3publicapi.models.reference import Reference
from form3publicapi.models.reimbursement_account_holding_entity import ReimbursementAccountHoldingEntity
from form3publicapi.models.senders_correspondent_account_holding_entity import SendersCorrespondentAccountHoldingEntity
from form3publicapi.models.settlement import Settlement
from form3publicapi.models.structured_reference import StructuredReference
from form3publicapi.models.swift import Swift
from form3publicapi.models.ultimate_entity import UltimateEntity
from form3publicapi.models.user_defined_data import UserDefinedData


class PaymentAttributes(object):

    """Implementation of the 'PaymentAttributes' model.

    TODO: type model description here.

    Attributes:
        agents (List[Agent]): Block to represent a Financial Institution/agent
            in the payment chain
        amount (str): Amount of money moved between the instructing agent and
            instructed agent
        batch_booking_indicator (str): TODO: type description here.
        batch_id (str): TODO: type description here.
        batch_type (str): TODO: type description here.
        beneficiary_party (BeneficiaryParty1): TODO: type description here.
        category_purpose (str): Category purpose in proprietary form.
            Specifies the high level purpose of the instruction. Cannot be
            used at the same time as `category_purpose_coded`.
        category_purpose_coded (str): Category purpose in a coded form.
            Specifies the high level purpose of the instruction. Cannot be
            used at the same time as `category_purpose`.
        charges_information (ChargesInformation): TODO: type description
            here.
        clearing_id (str): Unique identifier for organisations collecting
            payments
        currency (str): Currency of the transaction amount. Currency code as
            defined in [ISO
            4217](http://www.iso.org/iso/home/standards/currency_codes.htm)
        debtor_party (DebtorParty): TODO: type description here.
        end_to_end_reference (str): Unique identification, as assigned by the
            initiating party, to unambiguously identify the transaction. This
            identification is passed on, unchanged, throughout the entire
            end-to-end chain.
        file_number (str): TODO: type description here.
        fx (Fx): TODO: type description here.
        instruction_id (str): Unique identification, as assigned by the
            initiating party to unambiguously identify the transaction. This
            identification is an point-to-point reference and is passed on,
            unchanged, throughout the entire chain. Cannot include leading,
            trailing or internal spaces.
        intermediary_bank (IntermediaryBankAccountHoldingEntity): TODO: type
            description here.
        numeric_reference (str): Numeric reference field, see scheme specific
            descriptions for usage
        payment_acceptance_datetime (datetime): Timestamp of when the payment
            instruction meets the set processing conditions. Format:
            YYYY-MM-DDThh:mm:ss:mmm+hh:mm
        payment_purpose (str): Purpose of the payment in a proprietary form
        payment_purpose_coded (str): Purpose of the payment in a coded form
        payment_scheme (str): Clearing infrastructure through which the
            payment instruction is to be processed. Default for given
            organisation ID is used if left empty. Has to be a valid [scheme
            identifier](http://draft-api-docs.form3.tech/api.html#enumerations-
            schemes).
        payment_type (str): TODO: type description here.
        processing_date (date): Date on which the payment is to be debited
            from the debtor account. Formatted according to ISO 8601 format:
            YYYY-MM-DD.
        receivers_correspondent (ReceiversCorrespondentAccountHoldingEntity):
            TODO: type description here.
        reference (str): Payment reference for beneficiary use
        references (List[Reference]): Block to represent a list of references
        regulatory_reporting (str): Regulatory reporting information
        reimbursement (ReimbursementAccountHoldingEntity): TODO: type
            description here.
        remittance_information (str): Information supplied to enable the
            matching of an entry with the items that the transfer is intended
            to settle, such as commercial invoices in an accounts receivable
            system provided by the debtor for the beneficiary.
        scheme_payment_sub_type (str): The scheme specific payment [sub
            type](http://api-docs.form3.tech/api.html#enumerations-scheme-speci
            fic-payment-sub-types)
        scheme_payment_type (str): The [scheme-specific payment
            type](#enumerations-scheme-payment-types)
        scheme_processing_date (date): Date on which the payment is processed
            by the scheme. Only used if different from `processing_date`.
        scheme_transaction_id (str): Unique identification, as assigned by the
            first instructing agent, to unambiguously identify the transaction
            that is passed on, unchanged, throughout the entire interbank
            chain.
        senders_correspondent (SendersCorrespondentAccountHoldingEntity):
            TODO: type description here.
        settlement (Settlement): Specifies the details on how the settlement
            of the transaction between the instructing agent and the
            instructed agent is completed
        structured_reference (StructuredReference): TODO: type description
            here.
        swift (Swift): TODO: type description here.
        ultimate_beneficiary (UltimateEntity): TODO: type description here.
        ultimate_debtor (UltimateEntity): TODO: type description here.
        unique_scheme_id (str): The scheme-specific unique transaction ID.
            Populated by the scheme.
        user_defined_data (List[UserDefinedData]): All purpose list of
            key-value pairs specific data stored on the payment.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "agents": 'agents',
        "amount": 'amount',
        "batch_booking_indicator": 'batch_booking_indicator',
        "batch_id": 'batch_id',
        "batch_type": 'batch_type',
        "beneficiary_party": 'beneficiary_party',
        "category_purpose": 'category_purpose',
        "category_purpose_coded": 'category_purpose_coded',
        "charges_information": 'charges_information',
        "clearing_id": 'clearing_id',
        "currency": 'currency',
        "debtor_party": 'debtor_party',
        "end_to_end_reference": 'end_to_end_reference',
        "file_number": 'file_number',
        "fx": 'fx',
        "instruction_id": 'instruction_id',
        "intermediary_bank": 'intermediary_bank',
        "numeric_reference": 'numeric_reference',
        "payment_acceptance_datetime": 'payment_acceptance_datetime',
        "payment_purpose": 'payment_purpose',
        "payment_purpose_coded": 'payment_purpose_coded',
        "payment_scheme": 'payment_scheme',
        "payment_type": 'payment_type',
        "processing_date": 'processing_date',
        "receivers_correspondent": 'receivers_correspondent',
        "reference": 'reference',
        "references": 'references',
        "regulatory_reporting": 'regulatory_reporting',
        "reimbursement": 'reimbursement',
        "remittance_information": 'remittance_information',
        "scheme_payment_sub_type": 'scheme_payment_sub_type',
        "scheme_payment_type": 'scheme_payment_type',
        "scheme_processing_date": 'scheme_processing_date',
        "scheme_transaction_id": 'scheme_transaction_id',
        "senders_correspondent": 'senders_correspondent',
        "settlement": 'settlement',
        "structured_reference": 'structured_reference',
        "swift": 'swift',
        "ultimate_beneficiary": 'ultimate_beneficiary',
        "ultimate_debtor": 'ultimate_debtor',
        "unique_scheme_id": 'unique_scheme_id',
        "user_defined_data": 'user_defined_data'
    }

    _optionals = [
        'agents',
        'amount',
        'batch_booking_indicator',
        'batch_id',
        'batch_type',
        'beneficiary_party',
        'category_purpose',
        'category_purpose_coded',
        'charges_information',
        'clearing_id',
        'currency',
        'debtor_party',
        'end_to_end_reference',
        'file_number',
        'fx',
        'instruction_id',
        'intermediary_bank',
        'numeric_reference',
        'payment_acceptance_datetime',
        'payment_purpose',
        'payment_purpose_coded',
        'payment_scheme',
        'payment_type',
        'processing_date',
        'receivers_correspondent',
        'reference',
        'references',
        'regulatory_reporting',
        'reimbursement',
        'remittance_information',
        'scheme_payment_sub_type',
        'scheme_payment_type',
        'scheme_processing_date',
        'scheme_transaction_id',
        'senders_correspondent',
        'settlement',
        'structured_reference',
        'swift',
        'ultimate_beneficiary',
        'ultimate_debtor',
        'unique_scheme_id',
        'user_defined_data',
    ]

    def __init__(self,
                 agents=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 batch_booking_indicator=APIHelper.SKIP,
                 batch_id=APIHelper.SKIP,
                 batch_type=APIHelper.SKIP,
                 beneficiary_party=APIHelper.SKIP,
                 category_purpose=APIHelper.SKIP,
                 category_purpose_coded=APIHelper.SKIP,
                 charges_information=APIHelper.SKIP,
                 clearing_id=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 debtor_party=APIHelper.SKIP,
                 end_to_end_reference=APIHelper.SKIP,
                 file_number=APIHelper.SKIP,
                 fx=APIHelper.SKIP,
                 instruction_id=APIHelper.SKIP,
                 intermediary_bank=APIHelper.SKIP,
                 numeric_reference=APIHelper.SKIP,
                 payment_acceptance_datetime=APIHelper.SKIP,
                 payment_purpose=APIHelper.SKIP,
                 payment_purpose_coded=APIHelper.SKIP,
                 payment_scheme=APIHelper.SKIP,
                 payment_type=APIHelper.SKIP,
                 processing_date=APIHelper.SKIP,
                 receivers_correspondent=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 references=APIHelper.SKIP,
                 regulatory_reporting=APIHelper.SKIP,
                 reimbursement=APIHelper.SKIP,
                 remittance_information=APIHelper.SKIP,
                 scheme_payment_sub_type=APIHelper.SKIP,
                 scheme_payment_type=APIHelper.SKIP,
                 scheme_processing_date=APIHelper.SKIP,
                 scheme_transaction_id=APIHelper.SKIP,
                 senders_correspondent=APIHelper.SKIP,
                 settlement=APIHelper.SKIP,
                 structured_reference=APIHelper.SKIP,
                 swift=APIHelper.SKIP,
                 ultimate_beneficiary=APIHelper.SKIP,
                 ultimate_debtor=APIHelper.SKIP,
                 unique_scheme_id=APIHelper.SKIP,
                 user_defined_data=APIHelper.SKIP):
        """Constructor for the PaymentAttributes class"""

        # Initialize members of the class
        if agents is not APIHelper.SKIP:
            self.agents = agents 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if batch_booking_indicator is not APIHelper.SKIP:
            self.batch_booking_indicator = batch_booking_indicator 
        if batch_id is not APIHelper.SKIP:
            self.batch_id = batch_id 
        if batch_type is not APIHelper.SKIP:
            self.batch_type = batch_type 
        if beneficiary_party is not APIHelper.SKIP:
            self.beneficiary_party = beneficiary_party 
        if category_purpose is not APIHelper.SKIP:
            self.category_purpose = category_purpose 
        if category_purpose_coded is not APIHelper.SKIP:
            self.category_purpose_coded = category_purpose_coded 
        if charges_information is not APIHelper.SKIP:
            self.charges_information = charges_information 
        if clearing_id is not APIHelper.SKIP:
            self.clearing_id = clearing_id 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if debtor_party is not APIHelper.SKIP:
            self.debtor_party = debtor_party 
        if end_to_end_reference is not APIHelper.SKIP:
            self.end_to_end_reference = end_to_end_reference 
        if file_number is not APIHelper.SKIP:
            self.file_number = file_number 
        if fx is not APIHelper.SKIP:
            self.fx = fx 
        if instruction_id is not APIHelper.SKIP:
            self.instruction_id = instruction_id 
        if intermediary_bank is not APIHelper.SKIP:
            self.intermediary_bank = intermediary_bank 
        if numeric_reference is not APIHelper.SKIP:
            self.numeric_reference = numeric_reference 
        if payment_acceptance_datetime is not APIHelper.SKIP:
            self.payment_acceptance_datetime = APIHelper.apply_datetime_converter(payment_acceptance_datetime, APIHelper.RFC3339DateTime) if payment_acceptance_datetime else None 
        if payment_purpose is not APIHelper.SKIP:
            self.payment_purpose = payment_purpose 
        if payment_purpose_coded is not APIHelper.SKIP:
            self.payment_purpose_coded = payment_purpose_coded 
        if payment_scheme is not APIHelper.SKIP:
            self.payment_scheme = payment_scheme 
        if payment_type is not APIHelper.SKIP:
            self.payment_type = payment_type 
        if processing_date is not APIHelper.SKIP:
            self.processing_date = processing_date 
        if receivers_correspondent is not APIHelper.SKIP:
            self.receivers_correspondent = receivers_correspondent 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if references is not APIHelper.SKIP:
            self.references = references 
        if regulatory_reporting is not APIHelper.SKIP:
            self.regulatory_reporting = regulatory_reporting 
        if reimbursement is not APIHelper.SKIP:
            self.reimbursement = reimbursement 
        if remittance_information is not APIHelper.SKIP:
            self.remittance_information = remittance_information 
        if scheme_payment_sub_type is not APIHelper.SKIP:
            self.scheme_payment_sub_type = scheme_payment_sub_type 
        if scheme_payment_type is not APIHelper.SKIP:
            self.scheme_payment_type = scheme_payment_type 
        if scheme_processing_date is not APIHelper.SKIP:
            self.scheme_processing_date = scheme_processing_date 
        if scheme_transaction_id is not APIHelper.SKIP:
            self.scheme_transaction_id = scheme_transaction_id 
        if senders_correspondent is not APIHelper.SKIP:
            self.senders_correspondent = senders_correspondent 
        if settlement is not APIHelper.SKIP:
            self.settlement = settlement 
        if structured_reference is not APIHelper.SKIP:
            self.structured_reference = structured_reference 
        if swift is not APIHelper.SKIP:
            self.swift = swift 
        if ultimate_beneficiary is not APIHelper.SKIP:
            self.ultimate_beneficiary = ultimate_beneficiary 
        if ultimate_debtor is not APIHelper.SKIP:
            self.ultimate_debtor = ultimate_debtor 
        if unique_scheme_id is not APIHelper.SKIP:
            self.unique_scheme_id = unique_scheme_id 
        if user_defined_data is not APIHelper.SKIP:
            self.user_defined_data = user_defined_data 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        agents = None
        if dictionary.get('agents') is not None:
            agents = [Agent.from_dictionary(x) for x in dictionary.get('agents')]
        else:
            agents = APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        batch_booking_indicator = dictionary.get("batch_booking_indicator") if dictionary.get("batch_booking_indicator") else APIHelper.SKIP
        batch_id = dictionary.get("batch_id") if dictionary.get("batch_id") else APIHelper.SKIP
        batch_type = dictionary.get("batch_type") if dictionary.get("batch_type") else APIHelper.SKIP
        beneficiary_party = BeneficiaryParty1.from_dictionary(dictionary.get('beneficiary_party')) if 'beneficiary_party' in dictionary.keys() else APIHelper.SKIP
        category_purpose = dictionary.get("category_purpose") if dictionary.get("category_purpose") else APIHelper.SKIP
        category_purpose_coded = dictionary.get("category_purpose_coded") if dictionary.get("category_purpose_coded") else APIHelper.SKIP
        charges_information = ChargesInformation.from_dictionary(dictionary.get('charges_information')) if 'charges_information' in dictionary.keys() else APIHelper.SKIP
        clearing_id = dictionary.get("clearing_id") if dictionary.get("clearing_id") else APIHelper.SKIP
        currency = dictionary.get("currency") if dictionary.get("currency") else APIHelper.SKIP
        debtor_party = DebtorParty.from_dictionary(dictionary.get('debtor_party')) if 'debtor_party' in dictionary.keys() else APIHelper.SKIP
        end_to_end_reference = dictionary.get("end_to_end_reference") if dictionary.get("end_to_end_reference") else APIHelper.SKIP
        file_number = dictionary.get("file_number") if dictionary.get("file_number") else APIHelper.SKIP
        fx = Fx.from_dictionary(dictionary.get('fx')) if 'fx' in dictionary.keys() else APIHelper.SKIP
        instruction_id = dictionary.get("instruction_id") if dictionary.get("instruction_id") else APIHelper.SKIP
        intermediary_bank = IntermediaryBankAccountHoldingEntity.from_dictionary(dictionary.get('intermediary_bank')) if 'intermediary_bank' in dictionary.keys() else APIHelper.SKIP
        numeric_reference = dictionary.get("numeric_reference") if dictionary.get("numeric_reference") else APIHelper.SKIP
        payment_acceptance_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("payment_acceptance_datetime")).datetime if dictionary.get("payment_acceptance_datetime") else APIHelper.SKIP
        payment_purpose = dictionary.get("payment_purpose") if dictionary.get("payment_purpose") else APIHelper.SKIP
        payment_purpose_coded = dictionary.get("payment_purpose_coded") if dictionary.get("payment_purpose_coded") else APIHelper.SKIP
        payment_scheme = dictionary.get("payment_scheme") if dictionary.get("payment_scheme") else APIHelper.SKIP
        payment_type = dictionary.get("payment_type") if dictionary.get("payment_type") else APIHelper.SKIP
        processing_date = dateutil.parser.parse(dictionary.get('processing_date')).date() if dictionary.get('processing_date') else APIHelper.SKIP
        receivers_correspondent = ReceiversCorrespondentAccountHoldingEntity.from_dictionary(dictionary.get('receivers_correspondent')) if 'receivers_correspondent' in dictionary.keys() else APIHelper.SKIP
        reference = dictionary.get("reference") if dictionary.get("reference") else APIHelper.SKIP
        references = None
        if dictionary.get('references') is not None:
            references = [Reference.from_dictionary(x) for x in dictionary.get('references')]
        else:
            references = APIHelper.SKIP
        regulatory_reporting = dictionary.get("regulatory_reporting") if dictionary.get("regulatory_reporting") else APIHelper.SKIP
        reimbursement = ReimbursementAccountHoldingEntity.from_dictionary(dictionary.get('reimbursement')) if 'reimbursement' in dictionary.keys() else APIHelper.SKIP
        remittance_information = dictionary.get("remittance_information") if dictionary.get("remittance_information") else APIHelper.SKIP
        scheme_payment_sub_type = dictionary.get("scheme_payment_sub_type") if dictionary.get("scheme_payment_sub_type") else APIHelper.SKIP
        scheme_payment_type = dictionary.get("scheme_payment_type") if dictionary.get("scheme_payment_type") else APIHelper.SKIP
        scheme_processing_date = dateutil.parser.parse(dictionary.get('scheme_processing_date')).date() if dictionary.get('scheme_processing_date') else APIHelper.SKIP
        scheme_transaction_id = dictionary.get("scheme_transaction_id") if dictionary.get("scheme_transaction_id") else APIHelper.SKIP
        senders_correspondent = SendersCorrespondentAccountHoldingEntity.from_dictionary(dictionary.get('senders_correspondent')) if 'senders_correspondent' in dictionary.keys() else APIHelper.SKIP
        settlement = Settlement.from_dictionary(dictionary.get('settlement')) if 'settlement' in dictionary.keys() else APIHelper.SKIP
        structured_reference = StructuredReference.from_dictionary(dictionary.get('structured_reference')) if 'structured_reference' in dictionary.keys() else APIHelper.SKIP
        swift = Swift.from_dictionary(dictionary.get('swift')) if 'swift' in dictionary.keys() else APIHelper.SKIP
        ultimate_beneficiary = UltimateEntity.from_dictionary(dictionary.get('ultimate_beneficiary')) if 'ultimate_beneficiary' in dictionary.keys() else APIHelper.SKIP
        ultimate_debtor = UltimateEntity.from_dictionary(dictionary.get('ultimate_debtor')) if 'ultimate_debtor' in dictionary.keys() else APIHelper.SKIP
        unique_scheme_id = dictionary.get("unique_scheme_id") if dictionary.get("unique_scheme_id") else APIHelper.SKIP
        user_defined_data = None
        if dictionary.get('user_defined_data') is not None:
            user_defined_data = [UserDefinedData.from_dictionary(x) for x in dictionary.get('user_defined_data')]
        else:
            user_defined_data = APIHelper.SKIP
        # Return an object of this model
        return cls(agents,
                   amount,
                   batch_booking_indicator,
                   batch_id,
                   batch_type,
                   beneficiary_party,
                   category_purpose,
                   category_purpose_coded,
                   charges_information,
                   clearing_id,
                   currency,
                   debtor_party,
                   end_to_end_reference,
                   file_number,
                   fx,
                   instruction_id,
                   intermediary_bank,
                   numeric_reference,
                   payment_acceptance_datetime,
                   payment_purpose,
                   payment_purpose_coded,
                   payment_scheme,
                   payment_type,
                   processing_date,
                   receivers_correspondent,
                   reference,
                   references,
                   regulatory_reporting,
                   reimbursement,
                   remittance_information,
                   scheme_payment_sub_type,
                   scheme_payment_type,
                   scheme_processing_date,
                   scheme_transaction_id,
                   senders_correspondent,
                   settlement,
                   structured_reference,
                   swift,
                   ultimate_beneficiary,
                   ultimate_debtor,
                   unique_scheme_id,
                   user_defined_data)
