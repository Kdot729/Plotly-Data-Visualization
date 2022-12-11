function check_website(choosen_website, selected_address)
{   
    
    for(let i = 0; i < selected_address.length; i++)
    {
    if (choosen_website == "Zapper")
        {
        //Example Website is https://zapper.fi/account/0xb3aa9923489bc2bfec323bf05346acd4afbc92a0?tab=nft&collectionToggle=collection
        let link = `https://zapper.fi/account/${selected_address[i]}?tab=nft&network=ethereum&collectionToggle=collection`;
        link_website(link, selected_address[i]);
        }
    else if (choosen_website == "Prosper-Circle")
        {
        //Example Website is https://prospercircle.com/wallet/0xb3aa9923489bc2bfec323bf05346acd4afbc92a0
        let link = `https://prospercircle.com/wallet/${selected_address[i]}`;
        link_website(link, selected_address[i]);
        }
    else if (choosen_website == "NFT-Go")
        {
        //Example Website is https://nftgo.io/account/ETH/0xB3aA9923489Bc2BFEc323Bf05346AcD4afbc92A0/NFT
        let link = `https://nftgo.io/account/ETH/${selected_address[i]}/NFT`;
        link_website(link, selected_address[i]);
        }
    else if (choosen_website == "OpenSea")
        {
        //Example Website is https://opensea.io/0xB3aA9923489Bc2BFEc323Bf05346AcD4afbc92A0
        let link = `https://opensea.io/${selected_address[i]}`;
        link_website(link, selected_address[i]);
        }
    else if (choosen_website == "Blur")
        {
        //Example Website is https://blur.io/0xb3aa9923489bc2bfec323bf05346acd4afbc92a0
        let link = `https://blur.io/${selected_address[i]}`;
        link_website(link, selected_address[i]);
        }
    };
};

function link_website(link, address){

    //Note Split the link by . or /. Then get the second index which should be the website name
    let website_name = (link.split(/[.|/]/))[2]; 
    let identifier = `${website_name}-${address}`;
    
    $("#badge-area").append('<a href="' + link + '" class="custom-badge-pill" value="' + identifier + '" target="_blank" id="' + identifier + '"></a>');
    $(`#${identifier}`).text(address.substr(0, 6));
};

function changed_website(){
        //Note This is neccesary because without it will include Zapper website and the new website, essentiatly doubling the actually amount of badges need
      //Note We only need the badges from the new website so .empty() is neccesary in this function too because we never call update_page which has $('#badge-area').empty()
      $("#badge-area").empty();
      if ($("#Website").val() == "Blur")
          alert("Blur requires you to connect a wallet to use. If you're not comfortable with that they use the other sites");
      if (($("#Address").val()).length != 0)
          check_website($("#Website").val(), $("#Address").val())
}

export {check_website, changed_website}