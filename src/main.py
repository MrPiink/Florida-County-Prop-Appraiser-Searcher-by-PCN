from itertools import count
from re import M
import yaml  # pip install pyyaml
from counties import Counties


def main():
    """The main file loads the config.yaml and then creates all the instances for each class depending on if the config says to
    and then starts the search for each county in order."""
    config = open("config.yml", "r")
    county_settings = yaml.load(config, Loader=yaml.FullLoader)

    if county_settings["Brevard"]["search"]:

        brevard = Counties(
            "Brevard",
            "https://www.bcpao.us/PropertySearch/#/nav/Search",
            county_settings["Brevard"]["row_start"],
            county_settings["Brevard"]["row_end"],
            "logs/full logs/brevard_log_file.txt",
            "logs/success logs/brevard_log_file.txt",
            "#txtPropertySearch_Pid",
            is_brevard=True
        )

        brevard.start()

    if county_settings["Broward"]["search"]:

        broward = Counties(
            "Broward",
            "https://web.bcpa.net/BcpaClient/#/Record-Search",
            county_settings["Broward"]["row_start"],
            county_settings["Broward"]["row_end"],
            "logs/full logs/broward_log_file.txt",
            "logs/success logs/broward_log_file.txt",
            "#txtField",
            is_broward=True
        )

        broward.start()

    if county_settings["Duval"]["search"]:

        duval = Counties(
            "Duval",
            "https://paopropertysearch.coj.net/Basic/Search.aspx",
            county_settings["Duval"]["row_start"],
            county_settings["Duval"]["row_end"],
            "logs/full logs/duval_log_file.txt",
            "logs/success logs/duval_log_file.txt",
            None,
            is_duval=True,
            is_select_property=True,
            property_result_css="#ctl00_cphBody_gridResults > tbody > tr:nth-child(2) > td:nth-child(1) > a"
        )

        duval.start()

    if county_settings["Hillsborough"]["search"]:

        hillsborough = Counties(
            "Hillsborough",
            "https://gis.hcpafl.org/propertysearch/#/nav/Basic%20Search",
            county_settings["Hillsborough"]["row_start"],
            county_settings["Hillsborough"]["row_end"],
            "logs/full logs/hillsborough_log_file.txt",
            "logs/success logs/hillsborough_log_file.txt",
            "#basic > label:nth-child(4) > input.pin-sized.ui-autocomplete-input",
            is_hillsborough=True,
            is_choose_pcn_search=True,
            choose_pcn_css="#basic > div > label:nth-child(2) > input[type=radio]",
            is_select_property=True,
            property_result_css="#table-basic-results > tbody > tr > td.link.multiline"
        )

        hillsborough.start()

    if county_settings["Lee"]["search"]:

        lee = Counties(
            "Lee",
            "https://www.leepa.org/Search/PropertySearch.aspx",
            county_settings["Lee"]["row_start"],
            county_settings["Lee"]["row_end"],
            "logs/full logs/lee_log_file.txt",
            "logs/success logs/lee_log_file.txt",
            "#ctl00_BodyContentPlaceHolder_WebTab1_tmpl0_STRAPTextBox",
            is_lee=True,
            is_select_property=True,
            property_result_css="#ctl00_BodyContentPlaceHolder_WebTab1 > div > div:nth-child(1) > div:nth-child(2) > table > tbody > tr > td:nth-child(4) > div > div:nth-child(1) > a",
            agree_button_css="#btnContinue"
        )

        lee.start()

    if county_settings["Marion"]["search"]:

        marion = Counties(
            "Marion",
            "https://www.pa.marion.fl.us/PropertySearch.aspx",
            county_settings["Marion"]["row_start"],
            county_settings["Marion"]["row_end"],
            "logs/full logs/marion_log_file.txt",
            "logs/success logs/marion_log_file.txt",
            "#MCPAMaster_MCPAContent_txtParm",
            choose_pcn_css="#MCPAMaster_MCPAContent_rblSearchBy_2",
            is_choose_pcn_search=True,
            is_marion=True,
            is_select_property=True,
            property_result_css="#srch > table.mctable > tbody > tr > td:nth-child(1) > a"
        )

        marion.start()

    if county_settings["Miami-Dade"]["search"]:

        miami_dade = Counties(
            "Miami-Dade",
            "https://www.miamidade.gov/Apps/PA/propertysearch/#/",
            county_settings["Miami-Dade"]["row_start"],
            county_settings["Miami-Dade"]["row_end"],
            "logs/full logs/miami-dade_log_file.txt",
            "logs/success logs/miami-dade_log_file.txt",
            "#search_box",
            is_miami_dade=True
        )

        miami_dade.start()

    if county_settings["Orange"]["search"]:

        orange = Counties(
            "Orange",
            "https://ocpaweb.ocpafl.org/parcelsearch",
            county_settings["Orange"]["row_start"],
            county_settings["Orange"]["row_end"],
            "logs/full logs/orange_log_file.txt",
            "logs/success logs/orange_log_file.txt",
            "#ParcelID",
            is_orange=True
        )

        orange.start()

    if county_settings["Osceola"]["search"]:

        osceola = Counties(
            "Osceola",
            "https://ira.property-appraiser.org/PropertySearch/",
            county_settings["Osceola"]["row_start"],
            county_settings["Osceola"]["row_end"],
            "logs/full logs/osceola_log_file.txt",
            "logs/success logs/osceola_log_file.txt",
            "#txtParcel",
            is_select_property=True,
            property_result_css="#search-result-table > tbody > tr",
            is_osceola=True
        )

        osceola.start()

    if county_settings["Palm Beach"]["search"]:

        palmbeach = Counties(
            "Palm Beach",
            "https://www.pbcgov.org/papa/Asps/GeneralAdvSrch/SearchPage.aspx?f=a",
            county_settings["Palm Beach"]["row_start"],
            county_settings["Palm Beach"]["row_end"],
            "logs/full logs/palmbeach_log_file.txt",
            "logs/success logs/palmbeach_log_file.txt",
            "#MainContent_txtParcel",
            is_palmbeach=True
        )

        palmbeach.start()

    if county_settings["Pasco"]["search"]:

        pasco = Counties(
            "Pasco",
            "https://search.pascopa.com/",
            county_settings["Pasco"]["row_start"],
            county_settings["Pasco"]["row_end"],
            "logs/full logs/pasco_log_file.txt",
            "logs/success logs/pasco_log_file.txt",
            None,
            is_pasco=True
        )

        pasco.start()

    if county_settings["Polk"]["search"]:

        polk = Counties(
            "Polk",
            "https://www.polkpa.org/CamaDisplay.aspx?OutputMode=Input&searchType=RealEstate&page=FindByID",
            county_settings["Polk"]["row_start"],
            county_settings["Polk"]["row_end"],
            "logs/full logs/polk_log_file.txt",
            "logs/success logs/polk_log_file.txt",
            "#parcelID",
            is_select_property=True,
            property_result_css="#CamaDisplayArea > div:nth-child(5) > table > tbody > tr.tr1 > td.parcelid.highlight > a",
            is_polk=True
        )
        polk.start()

    if county_settings["Saint Lucie"]["search"]:

        saint_lucie = Counties(
            "Saint Lucie",
            "https://www.paslc.gov/property-search/real-estate/parcel",
            county_settings["Saint Lucie"]["row_start"],
            county_settings["Saint Lucie"]["row_end"],
            "logs/full logs/saint_lucie_log_file.txt",
            "logs/success logs/saint_lucie_log_file.txt",
            "k-textbox",
            is_select_property=True,
            property_result_css="body > app-root > app-real-estate > app-parcel > div > app-grid-result > div.col > kendo-grid > div > kendo-grid-list > div > div.k-grid-table-wrap > table > tbody > tr > td.k-touch-action-auto.k-command-cell > button:nth-child(1)",
            is_saint_lucie=True,
            is_by_class=True
        )

        saint_lucie.start()

    if county_settings["Sarasota"]["search"]:

        sarasota = Counties(
            "Sarasota",
            "https://www.sc-pa.com/propertysearch",
            county_settings["Sarasota"]["row_start"],
            county_settings["Sarasota"]["row_end"],
            "logs/full logs/sarasota_log_file.txt",
            "logs/success logs/sarasota_log_file.txt",
            "#Strap",
            is_sarasota=True
        )

        sarasota.start()

    if county_settings["Seminole"]["search"]:

        seminole = Counties(
            "Seminole",
            "https://scpafl.org/",
            county_settings["Seminole"]["row_start"],
            county_settings["Seminole"]["row_end"],
            "logs/full logs/seminole_log_file.txt",
            "logs/success logs/seminole_log_file.txt",
            "#dnn_ctr443_View_txtParcel_I",
            is_seminole=True
        )

        seminole.start()

    if county_settings["Volusia"]["search"]:

        volusia = Counties(
            "Volusia",
            "https://vcpa.vcgov.org/search/real-property#gsc.tab=0",
            county_settings["Volusia"]["row_start"],
            county_settings["Volusia"]["row_end"],
            "logs/full logs/volusia_log_file.txt",
            "logs/success logs/volusia_log_file.txt",
            "#datatable_filter > label > input[type=search]",
            is_volusia=True,
            agree_button_css="#acceptDataDisclaimer",
            is_agree_button=True
        )

        volusia.start()


if __name__ == "__main__":
    main()
