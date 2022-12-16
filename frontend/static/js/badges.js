function website_changed()
{
    if ($("#Website").val() == "Blur")
        alert("Blur requires you to connect a wallet to use. If you're not comfortable with that they use the other sites");
    let badges_dictionary = create_badges_dictionary();
    link_website($("#Website").val(), badges_dictionary);
}

function create_badges_dictionary()
{
    //Note Get a list of all the anchor's id's
    let badges = $.map($('#badge-area > .custom-badge-pill'), badge_id => badge_id.id);
    let badges_dictionary = {};

    for(let i=0; i < badges.length; i++)
    {
    //Note badges[i] is the full address which is the key
    //Note badges[i].substr(0, 5) is the short address which is the value
    //Note substr range needs to match the slice in python. Start at 0 index and don't include the 5th index, so 5 characters
    badges_dictionary[badges[i]] = badges[i].substr(0, 5);
    }

    //Note Need to clear "badge-area" after creating the dictionary. If we clear "badge-area" before creating the dictionary then it will be empty because there's nothing there
    $("#badge-area").empty();
    return badges_dictionary;
}

function link_website(choosen_website, badges_dictionary)
{   
    // console.log(badges_dictionary)
    // console.log("in check website")

    //Note key is full_address. value is short_address
    for(let [key, value] of Object.entries(badges_dictionary))
    {
    if (choosen_website == "Zapper")
        {
        //Example Website is https://zapper.fi/account/0xb3aa9923489bc2bfec323bf05346acd4afbc92a0?tab=nft&collectionToggle=collection
        let link = `https://zapper.fi/account/${key}?tab=nft&network=ethereum&collectionToggle=collection`;
        $("#badge-area").append('<a href="' + link + '" class="custom-badge-pill" value="' + key + '" target="_blank" rel="noopener noreferrer" id="' + key + '">' + value + '</a>');
        }
    else if (choosen_website == "Prosper-Circle")
        {
        //Example Website is https://prospercircle.com/wallet/0xb3aa9923489bc2bfec323bf05346acd4afbc92a0
        let link = `https://prospercircle.com/wallet/${key}`;
        $("#badge-area").append('<a href="' + link + '" class="custom-badge-pill" value="' + key + '" target="_blank" rel="noopener noreferrer" id="' + key + '">' + value + '</a>');
        }
    else if (choosen_website == "NFT-Go")
        {
        //Example Website is https://nftgo.io/account/ETH/0xB3aA9923489Bc2BFEc323Bf05346AcD4afbc92A0/NFT
        let link = `https://nftgo.io/account/ETH/${key}/NFT`;
        $("#badge-area").append('<a href="' + link + '" class="custom-badge-pill" value="' + key + '" target="_blank" rel="noopener noreferrer" id="' + key + '">' + value + '</a>');
        }
    else if (choosen_website == "OpenSea")
        {
        //Example Website is https://opensea.io/0xB3aA9923489Bc2BFEc323Bf05346AcD4afbc92A0
        let link = `https://opensea.io/${key}`;
        $("#badge-area").append('<a href="' + link + '" class="custom-badge-pill" value="' + key + '" target="_blank" rel="noopener noreferrer" id="' + key + '">' + value + '</a>');
        }
    else if (choosen_website == "Blur")
        {
        //Example Website is https://blur.io/0xb3aa9923489bc2bfec323bf05346acd4afbc92a0
        let link = `https://blur.io/${key}`;
        $("#badge-area").append('<a href="' + link + '" class="custom-badge-pill" value="' + key + '" target="_blank" rel="noopener noreferrer" id="' + key + '">' + value + '</a>');
        }
    };
};

export {website_changed}